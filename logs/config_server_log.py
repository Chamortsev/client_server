
import sys
import os
import logging.handlers
sys.path.append(os.path.join(os.getcwd(), '..'))

log = logging.getLogger('server')
level_log = logging.ERROR

formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server.log')

stream_hand = logging.StreamHandler(sys.stderr)
stream_hand.setFormatter(formatter)
stream_hand.setLevel(level_log)

file_hand = logging.handlers.TimedRotatingFileHandler(path, encoding='utf8', interval=1, when='D')
file_hand.setFormatter(formatter)

log.setLevel(level_log)
log.addHandler(stream_hand)
log.addHandler(file_hand)


if __name__ == '__main__':
    log.critical('Критическая ошибка')
    log.error('Ошибка')
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
