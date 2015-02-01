#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-02-01 14:11:12
# Filename        : test.py
# Description     : 
from cattle import Cattle
c = Cattle('BbDU4MoFrx2YaF6tqBFmnKHFuDlq1EO-mm2ldlBm', 'WWdwgm4oRmOh_L9yKbyWplcUFaIGAZXk8e_UOtDs')
bucket = c.get_bucket('zjypan-0')
print bucket.private_url('http://7u2qd9.com1.z0.glb.clouddn.com/bg.jpg')

