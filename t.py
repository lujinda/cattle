#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-04 20:24:56
# Filename        : t.py
# Description     : 
from cattle.cattle import Cattle

c = Cattle('BbDU4MoFrx2YaF6tqBFmnKHFuDlq1EO-mm2ldlBm', 'WWdwgm4oRmOh_L9yKbyWplcUFaIGAZXk8e_UOtDs')
b = c.get_bucket('zjypan-0')
print b.empty()

