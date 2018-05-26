#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/10/18

import logging
from logging import handlers
#
# logging.basicConfig(format= '%(asctime)s-%(levelno)s-%(message)s',datefmt= '%m/%d/%Y %I:%M:%S %p',filename= 'log_test.log', level=logging.WARNING) #时间格式
#
# logging.warning('user [alex] attempted wrong password more than 3 times')
# logging.critical("server is down")
# logging.debug('just use debug')
# logging.info('bonnie login to the system')
# print('----------------------')
# ******************


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup"  in record.getMessage()



# 1.生成 logger 对象
logger = logging.getLogger('web')
logger.setLevel(logging.DEBUG)

# 1.1 把filter 对象填加到logger中
# logger.addFilter(IgnoreBackupLogFilter())
# 2.生成 hander 对象
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# fh = logging.FileHandler('web.log')
# fh = handlers.RotatingFileHandler('web.log',maxBytes=100, backupCount=5) 根据文件大小截断
fh =  handlers.TimedRotatingFileHandler('web.log',when='S',interval=5,backupCount=3)
# fh.setLevel(logging.INFO)
# 2.1 把hander对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

#3. 生成formmater 对象
# 3.1 把formater 对象绑定到handle 对象
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s-%(lineno)d - %(message)s')


ch.setFormatter(console_format)
fh.setFormatter(file_format)


logger.info('test log db backup 3')
logger.debug('test_log')
logger.error('error')
logger.warning('warning')


