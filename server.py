from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH, MAX_CONNECTIONS
from common.utils import create_message
from common.msgs import error_answer
from json import dumps, loads
from socket import socket, AF_INET, SOCK_STREAM
import sys
import logs.config_server_log
import logging

log = logging.getLogger('Server')

def get_port():
    try:
        listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        # listen_port = DEFAULT_PORT
        if 1024 < listen_port > 65535:
            raise ValueError
    except IndexError:
        log.critical('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        log.critical('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    return listen_port


def get_address():
    try:
        listen_address = sys.argv[sys.argv.index('-a') + 1]
        # listen_address = DEFAULT_IP_ADDRESS
    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать ip адрес.')
        sys.exit(1)
    except ValueError:
        print('Маска адреса *.*.*.*')
        sys.exit(1)
    return listen_address


def prepare_server():
    listen_port = DEFAULT_PORT
    if '-p' in sys.argv:
        listen_port = get_port()
    listen_address = DEFAULT_IP_ADDRESS
    if '-a' in sys.argv:
        listen_address = get_address()
    SERVER_SOCK = socket()
    SERVER_SOCK.bind((listen_address, listen_port))
    SERVER_SOCK.listen(MAX_CONNECTIONS)
    print(SERVER_SOCK.getsockname())
    return SERVER_SOCK


def main():
    SERVER_SOCK = prepare_server()
    print(f'Сервер {DEFAULT_IP_ADDRESS} запущен и слушает порт: {DEFAULT_PORT}')
    try:
        while True:
            client, client_address = SERVER_SOCK.accept()
            print(f'Установленно соединение с => {client_address}')
            data = client.recv(MAX_PACKAGE_LENGTH)
            try:
                msg = loads(data)
                event = msg['event']
                name = msg['name_client']
                print(f'Получено сообщение:\n{msg}')
            except Exception as e:
                event = 'error'
                name = None
                print(f'Ошибка: {e}')

            if event == 'start':
                answer = f'{name}, добро пожаловать в наш сервис'
                answer_data = {
                    'status': 200,
                    'answer': answer
                }
                send_msg = dumps(answer_data)
                client.send(send_msg.encode())
                try:
                    while True:
                        second_data = client.recv(MAX_PACKAGE_LENGTH)
                        try:
                            second_msg = loads(second_data)
                            event = second_msg['event']
                            print(f'Получено сообщение:\n{second_msg}')
                        except Exception as e:
                            event = 'error'
                            print(f'Ошибка {e}')
                        if event == 'message':
                            answer = f'Уважаемый {name}, ответ на все вопросы и вообще 42'
                            answer_data = {
                                'status': 200,
                                'answer': answer
                            }
                            send_msg = dumps(answer_data)
                            client.send(send_msg.encode())
                        else:
                            client.send(create_message(error_answer))
                except ConnectionAbortedError:
                    print(f'Клиент {client_address} разорвал соединение')
                    continue
            else:
                client.send(create_message(error_answer))
    finally:
        SERVER_SOCK.close()


if __name__ == '__main__':
    main()
