from time import time
# Шаблон сообщения начала диалога
start = {
    'name_client': 'Guest',
    'event': 'start',
}

# Шаблон отправки сообщения на сервер
message = {
    'name_client': 'Guest',
    'event': 'message',
    'text': 'Текст сообщения',
    'time': time(),
}

# Сообщение ошибка для JSON
fail_message = 'Не json для теста'

# Ответ от сервера если ошибка
error_answer = {
    'status': 400,
    'answer': 'Не верный формат запроса'
}

