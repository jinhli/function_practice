#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/10/18

import subprocess

#subprocess.run
# subprocess.call
# subprocess.Popen
a =subprocess.run(['df','-h'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True)

#管道
# a = subprocess.run('df -h|grep disk1',shell=True) #shell=True的意思是这条命令直接交给系统去执行，不需要python负责解析 call()方法
print(a.stdout)
