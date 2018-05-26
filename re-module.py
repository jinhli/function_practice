#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/8/18

import re

# f = open('model_info.txt')
#
# data = f.read()

# print(re.findall('1[0-9]{10}', data))

#检查电话号码合法
# s = input('input your phone_number:')
#
# res = re.match('^(13[0-9]{1}|145|147|15[0-9]{1}|17[0-9]{1}|18[0-9]{1})[0-9]{8}',s)
#
# if res:
#     print('the phone number is valid')
# else:
#     print('input the correct phone numeber:')


    # 检查邮件是否合法

s = input('input your email_address:')

res = re.match('\w+@\w+\.\w',s)

if res:
    print('the email_address is valid')
else:
    print('input the correct email_address:')