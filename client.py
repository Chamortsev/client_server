from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH
from common.msgs import start, message, fail_message
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import create_message
from json import loads
import random


def send_msg(my_message):
    CLIENT_SOCK.send(create_message(my_message))


if __name__ == '__main__':
    CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCK.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
    send_msg(start)
    data = CLIENT_SOCK.recv(MAX_PACKAGE_LENGTH)
    msg = loads(data)

    if msg['status'] == 200:
        print('Соединение установленно!')
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
