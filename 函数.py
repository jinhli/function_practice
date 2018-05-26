#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 4/9/18

#默认参数

# def stu_register(name,age,course = 'python',country = 'CN'):
#     print('registration info....')
#     print(name,age,country,course)
#
# stu_register('alex',22)
# stu_register('bonnie',23,'java')


#关键参数

# def stu_register(name,course,age,country = 'cn'):
#     print('registration info....')
#     print(name,age,country,course)
#
#
# stu_register('bonnie','C',age=28)


#包裹参数
# def stu_register(name,*args):
#     print('registration info....')
#     print(name,*args)
#
#
# stu_register('bonnie',*['python','java','c'])
#
# stu_register('bonnie','python','java','c')
#
# #如果参数中出现*args,传递的参数个数不是固定的，传来过的数是远祖

#**args
# def stu_register(name,*args,**kwargs):
#     print('registration info....')
#     print(name,args,kwargs)
#
# d={'degree':'primary school'}
# stu_register('bonnie',*['python','java','c'],**d)


#函数返回值, 遇到return 代表函数的终止,
#返回多个值会自动转成元组

# def stu_register(name,course,age):
#     print('registration info....')
#     print(name,course,age)
#     # if age >22:
#     #     return 'your age is too older'
#     # else:
#     #     return True
#     return name,age
#
#
# status=stu_register('bonnie','C',age=28)
# print(status)

#局部变量 就是定义再函数里的变量
#全局变量是定义再函数外边，或者可以说是以一级代码
#再函数内部，可以引用全局变量
#全局变量和局部变量同时在，局部变量优先级高
# name = 'bonnie'
#
# def change_name():
#     global name   #不建议你在函数里修改全局变量
#     name = '花花'
#     print('you name  is %s ' %name)
#
# change_name()
# print(name)


# 改列表，可以通过改值实现，但是不能重新赋值
# names = ['alex','black girl','peiqi']
#
# def change_name():
#     del names[2]
#     # names = ['alex','black girl']
#     print(names)
#
# change_name()
# print(names)

#嵌套函数
#由内向外一层一层找变量
# def func1():
#     print('alex')
#
#     def func2(): #不调用的话，只是把函数放入内存，并没有调用的话就不会执行
#         print('eric')
#     func2()
# func1()
# age = 18
# def func1():
#     # age =73
#     #print(age)
#
#     def func2(): #不调用的话，只是把函数放入内存，并没有调用的话就不会执行
#         # age = 84
#         print(age)
#     age =73
#     func2()
#
# func1()



#递归总结


#匿名函数
# data = list(range(10))
#
#
# print(list(filter(lambda n: n if n%2 ==1 else False, data)))

#
# level = 'L0'
# n = 22
#
#
# def func():
#     level = 'L1'
#     n = 33
#     print(locals())
#
#     def outer():
#         n = 44
#         level = 'L2'
#         print(locals(),n)
#
#         def inner():
#             level = 'L3'
#             print(locals(),n) #此外打印的n是多少？
#         inner()
#     outer()
#
#
# func()








