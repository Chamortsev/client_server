import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM

from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR
from common.utils import send_message, get_message


def get_answer(msg):
    if RESPONSE in msg:
        if msg[RESPONSE] == 200:
            return f'{RESPONSE: 200} from client'
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
            }
    raise ValueError


def create_session(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def get_server_address():
    global server_address
    try:
        if '-a' in sys.argv:
            server_address = sys.argv[sys.argv.index('addr')+1]
        else:
            server_address = DEFAULT_IP_ADDRESS
    except IndexError:
        print(f'Сервер указан не верно.Проверьте адрес сервера {server_address}')
        sys.exit(1)
    return server_address


def get_server_port():
    global server_port
    try:
        if '-p' in sys.argv:
            server_port = int(sys.argv[sys.argv.index('-p')+1])
            if 1024 < server_port > 65535:
                print(f'Указан неправильный порт{server_port}. Укажите в диапазоне 1024-65535')
                sys.exit(1)
        else:
            server_port = DEFAULT_PORT
    except IndexError:
        print('Укажите после параметра port номер порта')
        sys.exit(1)
    except ValueError:
        print(ValueError, 'ЧТо то пошло не так проверрьте входные параметры порта')
    return server_port


def get_client_socket():
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.connect((get_server_address(), get_server_port()))
    except Exception as e:
        print(f'Проверьте сервер и порт {e}')
        sys.exit(1)
    return transport


def main():

    try:
        client_socket = get_client_socket()
    except ConnectionRefusedError:
        print(f'Ошибка соединения с сервером{client_socket}. Проверьте запущен ли сервер')
        sys.exit(1)
    message_to_server = create_session()
    # print(message_to_server)
    # print(client_socket)
    # print(send_message(client_socket, message_to_server))
    send_message(client_socket, message_to_server)
    try:
        answer = get_answer(get_message(client_socket))
        print(answer)
    except (ValueError, json.JSONDecodeError) as e:
        print('Ошибка декодирования', e)
        # sys.exit(1)


if __name__ == '__main__':
    main()
