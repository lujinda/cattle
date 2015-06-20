#/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-06-20 10:38:56
# Filename      : test.py
# Description   : 
from cattle import Cattle

c = Cattle('BbDU4MoFrx2YaF6tqBFmnKHFuDlq1EO-mm2ldlBm', 'WWdwgm4oRmOh_L9yKbyWplcUFaIGAZXk8e_UOtDs')
bucket_name = 'imgdata'
b = c.get_bucket(bucket_name)
#print(b.ls())
#print(b.put_file('/etc/passwd', '你好吗', 'image/jpeg'))
print(b.rm('你好吗'))

