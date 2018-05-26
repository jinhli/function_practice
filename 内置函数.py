#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/7/18


#shutil
import shutil

# f = open('user_1.txt','r')
# f1 = open('user_1_new.txt','w')
#
# shutil.copyfileobj(f,f1)

#shutil.copyfile
shutil.copyfile('user_1.txt','user_1_new.txt')
#shutil.copy(src,dst)
# 拷贝文件和权限
#shutil.copy2(src,dst)

# shutil.move(src,dst)

# shutil.make_archive(base_name,format,path)

#
# import shelve
#
# f = shelve.open('user_1_new')
# names = ["alex", "rain", "test"]
# info = {'name':'alex','age':22}
# f["names"] = names  # 持久化列表
# f['info_dic'] = info
# f.close()

import xml.etree.ElementTree as ET

tree = ET.parse('xml_test')
root = tree.getroot()
# print(root.tag)
# print(dir(root))
# for child in root:
#     print('----------------', child.tag, child.attrib) #child.attrib =tag的属性
#     for i in child:
#         print(i.tag,i.text)  #i.text  tag 对应的内容

for node in root.iter('rank'):  #root.iter 想当可以迭代的
    print(node.tag,node.text)

# configparser 模块
# import configparser
#
# conf = configparser.ConfigParser()
# conf.read('tempest.conf')

#1.查
# print(conf.sections())
# print(conf.default_section)
# print(list(conf['identity'].items()))
#
# for i in conf['identity']:
#     print(i)

#2.增加

# conf.add_section('group3')
# conf['group3']['name'] = 'alex'
# # conf.write('tempest.conf','w')
# conf.write(open('tempest.conf','w'))

#3.删除
# conf.remove_option('group3','name') #删除选项
# conf.remove_section('group3') #删除section
# conf.write(open('tempest.conf','w'))

#4修改
#
# sec = conf.has_option('volume','max_microversion') #先判断是否存在
#
# if sec:
#     conf.set('volume','max_microversion','latest') #存在就修改相关的值
#
# conf.write(open('tempest.conf','w'))


# #hashlib 模块
# import hashlib
# m =hashlib.md5()
# m.update(b'bonnie')
# print(m.hexdigest())
#
#
# #loggin 模块
# # 记录运行日志
import logging
#
# logging.basicConfig(format= '%(asctime)s-%(levelno)s-%(message)s',datefmt= '%m/%d/%Y %I:%M:%S %p',filename= 'log_test.log', level=logging.WARNING) #时间格式
#
# logging.warning('user [alex] attempted wrong password more than 3 times')
# logging.critical("server is down")
# logging.debug('just use debug')
# logging.info('bonnie login to the system')
# print('----------------------')
# ******************


