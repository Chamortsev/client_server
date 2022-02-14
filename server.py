from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH, MAX_CONNECTIONS
from common.utils import create_message
from common.msgs import error_answer
from json import dumps, loads
from socket import socket

SERVER_SOCK = socket()
SERVER_SOCK.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
SERVER_SOCK.listen(MAX_CONNECTIONS)
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
