"""顾名思义为在内存中读写str，StringIO经常被用来作字符串的缓存"""

from io import StringIO
from io import BytesIO

# f1 = StringIO()      # 创建一个StringIO
# # 写入str：
# print(f.write('hello py1 '))
# print(f.write('hello py2 '))
# print(f.write('hello py3 '))


# 读取StringIO，可以用一个str初始化StringIO，再像文件一样读取：
f2 = StringIO('Hello,\nHi!\nGoodbye!')
print(f2.read())


# StringIO只能操作str，如果要操作二进制数据，就需要用BytesIO:
f3 = BytesIO()
print(f3.write('中文'.encode('utf-8')))
print(f3.getvalue())






