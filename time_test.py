#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/19/18

import time
import calendar
import datetime
# def get_time():

    # current_time = time.strftime('%Y-%m-%d',time.localtime())
current_time = datetime.datetime.now()
future = current_time + datetime.timedelta(weeks=4)

#
# print(future)
# # expire_date =
print(current_time.strftime('%Y-%m-%d'))
print(future.strftime('%Y-%m-%d'))
print(future.day)

# get_time()

a = calendar.isleap(2009)

b = calendar.weekday(2008,3,8)

c = calendar.monthrange(2008,4)

e = time.strptime('2018/4/4',"%Y/%m/%d")
f = time.mktime(e)

g = time.localtime()
h = time.strftime('%Y-%m-%d',g)
print(h)
