# encoding='utf-8'
# urllib的使用方法：

import urllib
from urllib.request import urlopen
from urllib.parse import urlencode


# 处理get请求，不传data：
url = 'http://127.0.0.1:1990/login'
data = {"username": "mosey", "password": 123456}

# 将字典类型的数据转变为url编码：
reg_data = urlencode(data)

# 通过urlopen()方法访问拼接好的url：
r1 = urlopen(url + '?' + reg_data)

# read()获取网页的内容,decode()转换返回数据的bytes格式：
r11 = r1.read().decode()


# 例：
r = urllib.request.urlopen('https://www.zhihu.com/')
# r.read()可以获取网页的内容
print(r.read().decode('utf-8'))















