import logging.config
from logx.config import LOG_CONFIG

def init_logger() -> logging.Logger:
    # 加载配置
    logging.config.dictConfig(LOG_CONFIG)

    # 获取指定logger
    logger = logging.getLogger('console')
    
    return logger