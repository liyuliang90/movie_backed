#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import logging
import logging.config

_logger_handler = "logging.handlers.TimedRotatingFileHandler"
_backupCount = 5

def logfile(filename):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(current_dir)
    return os.path.join(parent_dir, 'logs', filename)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": _logger_handler,
            "level": "DEBUG",
            "formatter": "simple",
            "filename": logfile('tmall.log'),
            "when": "midnight",
            "interval": 1,
            "backupCount": _backupCount,
            "encoding": 'utf-8'
        },
    },
    #"root": {
    #    'handlers': ['console', 'file'],
    #    'level': CONFIG.TTI_LOG_LEVEL,
    #    'propagate': False
    #},
    "loggers":{
        "tmall":{
            'handlers': ['file'],
            'level': "DEBUG",
            'propagate': False
        },
    }
}

def get_logger(name=None):
    logging.config.dictConfig(LOGGING_CONFIG)
    res_logger = logging.getLogger(name)
    return res_logger 

logger = get_logger('tmall')
