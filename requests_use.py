# requests 模块的使用方法


import requests
import json
# 获取某个网页，r为response对象,Requests会自动解码来自服务器的内容：
r1 = requests.get('https://api.github.com/events')

# 获取相应内容（以文本的方式）：
print(r1.text)
# 以字节的方式：
print(r1.content)

# 处理json内容：
print(r1.json())

# 检查请求是否成功；
print(r1.status_code)

# 获取网页编码：
print(r1.encoding)
# 修改网页编码：
r1.encoding = 'utf-8'


# 发送http post请求：
r2 = requests.post('http://httpbin.org/post', date={'key': 'value'})


# 定制请求头：
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r3 = requests.get(url, headers=headers)
# print(r3.headers)？


# 响应cookie：
r4 = requests.get(url)
print(r4.cookies['example_cookie_name'])

# 发送cookie到服务器:
url1 = 'http://m.ctrip.com/cookies'
cookies = dict(cookies_are='working')
r5 = requests.get(url1, cookies=cookies)


# 设置超时时间,经过以 timeout 参数设定的秒数时间之后停止等待响应：
r6 = requests.get('http://m.ctrip.com', timeout=0.001)


# 设置访问代理：
proxies = {"http": "http://10.10.10.10:8888",
           "https": "http://10.10.10.100:4444"}
r7 = requests.get('http://m.ctrip.com', proxies=proxies)







