import logging
import logging.config

def get_sum(x1, *x2):
    try:
        logger.debug('Зашли в метод get_sum со значениями - {}'.format(x1, x2))
        result = x1 + sum(x2)
        logger.debug('Вернули значение - {}'.format(result))
        return result
    except Exception as ex:
        logger.exception(ex)
        return None


logging.config.fileConfig('config.conf')
logger = logging.getLogger("logging")
logger.info('Программа запустилась')
print(get_sum(5, 0, "ы", 2, 3))
logger.info('Программа завершила свое выполнение')