import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(client):
    """  Утилита приёма и декодирования сообщения принимает байты выдаёт словарь, если принято что-то другое,
    отдаёт ошибку значения
    :param client:
    :return:
    """

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """
    print(sock)
    print(message)
    print(json.dumps(message))
    js_message = json.dumps(message)
    print(js_message.encode(ENCODING))
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)


def create_message(data_dict):
    msg = json.dumps(data_dict)
    msg_byte = msg.encode()
    return msg_byte
