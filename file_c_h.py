#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;

def create_c_h():
    z = input("请输入文件名...\n")
    h = open(z+'.h','w')
    c = open(z+'.c','w')
    h.write('// File Name:'+z+'.h\n'+\
'// Engineer: gus'+'\n'+\
'// Last Edit: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'+\
'// Revision: 0000'+'\n'+\
'// Copyright(c) by Fuji Xerox Co.,Ltd All rights reserved.'+'\n'+\
'\n'+\
'#ifndef '+z.upper()+'_H\n'+\
'#define '+z.upper()+'_H\n'+\
'\n'+\
'#endif\n')
    c.write('// File Name:'+z+'.c\n'+\
'// Engineer: gus'+'\n'+\
'// Last Edit: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'+\
'// Revision: 0000'+'\n'+\
'// Copyright(c) by Fuji Xerox Co.,Ltd All rights reserved.'+'\n'+\
'\n'+\
'\"#include '+z+'.h\"\n'+\
'\n')

create_c_h()

