#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 4/10/18

#深度查询
#打印所有的结点
#输入一个节点名字，沙河，你要遍历，真找到了就打印它，并返回True

# menus = [
#     {
#         'text':'北京',
#         'children':[
#             {'text':'朝阳','children':[]},
#             {'text':'昌平','children':[
#                 {'text':'沙河','children':[]},
#                 {'text':'回龙关','children':[]}
#             ]}
#         ]
#     },
#     {
#         'text':'上海',
#         'children':[
#             {'text':'宝山','children':[]},
#             {'text':'金山','children':[]}
#         ]
#     }
# ]
#
#
# def list_info(menus):
#     for i in menus:
#         print(i['text'],',')
#         if len(list(i['children']))>0:
#             menus = i['children']
#             list_info(menus)
#
# list_info(menus)

# print 函数
# s='我是花花'
# f= open('user_1.txt','a')
#
# print(s,'我是Bbonnie',sep='|',end='\n',file=f)
# print(s,sep='|',end='\n',file=f)