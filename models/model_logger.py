import logging

from datetime import datetime
from configure import config


logfile = f"{config['global']['log_path']}/{datetime.now().strftime('custom_%Y-%m-%d.log')}"

# 创建自动生成日志的日志记录器
# auto_logger = logging.getLogger('auto_logger')
# auto_logger.setLevel(logging.INFO)

# auto_handler = logging.FileHandler('auto.log')
# auto_logger.addHandler(auto_handler)

# 创建自定义日志的日志记录器
custom_logger = logging.getLogger('custom_logger')
custom_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

custom_handler = logging.FileHandler(logfile)
custom_handler.setFormatter(formatter)
custom_logger.addHandler(custom_handler)
