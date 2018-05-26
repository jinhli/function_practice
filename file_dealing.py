#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 4/8/18

# read
# f = open('model.txt','r')
#
# for line in f:
#     print(line.strip())
#
# f.close()

#write +append
# f = open('model_1.txt','r',encoding='utf-8')
# print(f.readable())

# f.write('\n'+'路飞学成1')
# f.close()


#r+ 都写模式

# f = open('model.txt','r+')
# data = f.read()
#
# print('content',data)
#
# f.write('\nnew line 1')
# f.write('\nnew line 2')
#
# print('content',f.read())
#
# f.close()


#w+ 写度模式

# readable()


#随意位置加入 ,缺点是可能会覆盖了之前的数据，不建议

# f = open('model.txt','r+')
#
# f.seek(10)
#
# f.write('edifer 333')
#
# f.close()


#占硬盘的插入方式
# import os
#
# f_name = 'model.txt'
# f_new_name = '%s.new' %f_name
#
# old_str = 'bonnie'
# new_str = '花花'
#
# f = open(f_name,'r')
# f_new = open(f_new_name,'w')
#
# for line in f:
#     if old_str in line:
#         line = line.replace(old_str,new_str)
#     f_new.write(line)
#
# f.close()
# f_new.close()
#
# os.rename(f_new_name,f_name)
# 占内存模式的

# f = open('model.txt','r+')
#
# data = f.read()
#
# new_data = data.replace('123', "huahua")
#
# print(new_data)
#
# f.seek(0)
#
# f.write(new_data)

# f.close()

# #homework_1
#
# import sys
# import os
#
# file_name = sys.argv[1]
# file_name_new = 'model_new.txt'
# f1 = open(file_name_new,'w')
#
# old_str = sys.argv[2]
# new_str = sys.argv[3]
#
# with open(file_name,'r') as f:
#     for line in f:
#         if old_str in line:
#             line = line.replace(old_str,new_str)
#             print(line)
#         f1.write(line)
#
# f1.close()
#
# os.rename(file_name_new,file_name)

#homework 2
user_info = []
count = 0
password_count = 0
passward_flag = True

f = open('model_1.txt','r')
f1 = open('user_1.txt','w')

while True:
    name = input('input your name >>').strip()
    for line in f:
        user_info = line.split()
        if name == user_info[0]:
            if user_info[2] == 'lock':
                exit("you have tried 3 time, please try next day'")
            else:
                while passward_flag:
                    passward = input('input your password>>').strip()
                    if passward == user_info[1]:
                        print('welcome')
                        exit()
                    else:
                        password_count+=1
                        if password_count == 3:
                            passward_flag = False
                else:
                    passward_flag = True
                    print('input 3 times for the wrong passward')
                    break

                line = line.replace('unlock','lock')
        # else:
        #     print('input your name again>>')
        f1.write(line)

    else:
            count+=1
f.close()
f1.close()
# print('you have tried 3 time')