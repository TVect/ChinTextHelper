#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午5:14
# @Author  : wanyuan.chen

import os
#os.remove("{}/{}".format(os.path.split(os.path.abspath(__file__))[0],"_dat.so"))
#lib_path = "{}/{}".format(os.path.split(os.path.abspath(__file__))[0],"_dat.so")
#print(lib_path)
if not os.path.isfile("{}/{}".format(os.path.split(os.path.abspath(__file__))[0],"_dat.so")):
    os.system("cd {} && bash my.make && cd -".format(os.path.split(os.path.abspath(__file__))[0]))
