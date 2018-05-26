#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/17/18

import hashlib


def passwd_md5(account, password):
    """

    :param account:
    :param password:
    :return:  MD5 密码
    """

    md5 = hashlib.md5(account.encode('utf-8'))  #带上用户名加密
    md5.update(password.encode('utf-8'))   #加上encode编码
    ret = md5.hexdigest()
    return ret


a = passwd_md5('tesla','1234')
print(a)

