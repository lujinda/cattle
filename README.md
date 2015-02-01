#cattle
<img src="http://assets.qiniu.com/qiniu-204x109.png" />

cattle是七牛的python第三方sdk，据根 [http://docs.qiniutek.com/v3/api/io/#upload](http://docs.qiniutek.com/v3/api/io/#upload) 和 [http://developer.qiniu.com/docs/v6/index.html](http://developer.qiniu.com/docs/v6/index.html) 这里面的api文档写的。比官方的用起来方便，功能也挺多的，一般的文件上传，下载，操作等都没什么问题。

###简单手册:
<pre>
from cattle import Cattle
cattle = Cattle(AK, SK)

获取bucket:
bucket = cattle.get_bucket(bucket_name)

列出所有文件：
cattle.ls_all(bucket_name) / bucket.ls_all()

列出前10个文件:
cattle.ls(bucket_name, limit=10) / bucket.ls(limit=10)

文件直传:
cattle.put_file(bucket_name, file_path = '/etc/passwd') / bucket.put(file_path = '/etc/passwd')

删除:
cattle.rm(bucket_name, key) / bucket.rm(key)

查看文件状态:
cattle.stat(bucket_name, key) / bucket.stat(key)

获取私有资源的文件下载地址:
cattle.private_url('http://域名/key', ttl = 3600) /bucket.private_url('http://域名/key', ttl = 3600) 

列出所有bucket:
cattle.list_bucket()

help(cattle.put_file):
put_file(self, scope, file_path, key=None, mime_type='', override=True, md5=False) method of cattle.cattle.Cattle instance
    直传文件
    如果不指定key，同时md5为False，则会以 file_path作为 key，如果指定了md5对内容做一个md5计算，以md5值作为key
    
</pre>

还有些其他的，大家自己看源码吧。

###安装

sudo python setup.py install

