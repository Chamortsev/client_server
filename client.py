from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH
from common.msgs import start, message, fail_message
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import create_message
from json import loads
import random
import sys


def send_msg(my_message):
    CLIENT_SOCK.send(create_message(my_message))


def get_serv_address():
    try:
        server_address = sys.argv[sys.argv.index('addr') + 1]
    except IndexError:
        print(
            'После параметра \'addr\'- необходимо указать адрес сервера.')
        sys.exit(1)
    return server_address


def get_serv_port():
    try:
        server_port = int(sys.argv[sys.argv.index('-p') + 1])
        print(server_port)
        if 1024 < server_port > 65535:
            print(
                'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)
    except IndexError:
        print('После параметра \'port\' необходимо указать номер порта.')
        sys.exit(1)

    return server_port


def prepare_client():
    server_address = DEFAULT_IP_ADDRESS
    if 'addr' in sys.argv:
        server_address = get_serv_address()
    server_port = DEFAULT_PORT
    if 'port' in sys.argv:
        server_port = get_serv_port()
    CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
    try:
        CLIENT_SOCK.connect((server_address, server_port))
    except Exception:
        print('Проверьте порт и сервер')
        sys.exit(1)
    return CLIENT_SOCK


if __name__ == '__main__':
    CLIENT_SOCK = prepare_client()
    send_msg(start)

    data = CLIENT_SOCK.recv(MAX_PACKAGE_LENGTH)
    msg = loads(data)

    if msg['status'] == 200:
        print(f'Соединение установленно! {CLIENT_SOCK}')
        print(f'***Получено сообщение от сервера***\n Статус: {msg["status"]}\n Сообщение: {msg["answer"]}')
        random_message = [message, fail_message][random.randint(0, 1)]
        print(f'Отправляем сообщение => {random_message}')
        send_msg(random_message)
        try:
            data_answer = CLIENT_SOCK.recv(MAX_PACKAGE_LENGTH)
        except socket.timeout:
            print('Не дождались сообщения')
        answer = loads(data_answer)
        status = answer["status"]
        msg_client = answer['answer']
        if status == 200:
            print(f'***Получено сообщение от сервера***\n Статус: {status}\n Сообщение: {msg_client}')
        else:
            print('Ошибка')
            print(f'Статус: {status}\n Сообщение: {msg_client}')
    else:
        print('Ошибка')
        print(f'Статус: {msg["status"]}\n Сообщение: {msg["answer"]}')
    CLIENT_SOCK.close()