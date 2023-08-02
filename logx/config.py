import logging


LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': 'ts=%(asctime)s level=%(levelname)s caller=%(filename)s:%(lineno)d msg="%(message)s"',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z'
        }
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': logging.INFO,
            'formatter': 'standard',
        }
    },
    'loggers':{
        'console': {
            'level': logging.INFO,
            'handlers': ['console_handler'],
            'propagate': False
        }
    }
}