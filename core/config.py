import os

__all__ = ['CONFIG']


class Config:
    LOG_LEVEL = str(os.environ.get('LOG_LEVEL', 'DEBUG')).upper()

    MYSQL_HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '123456')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'ticket')

CONFIG = Config()
