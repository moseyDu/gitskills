# coding:utf-8
# os模块包含普遍的操作系统功能,针对操作系统进行操作

import os

# # 获取当前的工作目录：
# print(os.getcwd())
#
# # 改变当前的工作目录：
# os.chdir('')
#
# # 指定文件夹中所有内容的名称列表：
# os.listdir('')
#
# # 创建文件夹：
# os.mkdir('')
#
# # 删除空目录：
# Os.rmdir('')
#
# # 文件夹重命名：
# os.rename('', '')
#
# # 获取系统的环境变量：
# os.getenv('PATH')
#
#
# # os.path:
# os.path.abspath(path)   # 将相对路径转化为绝对路径
# os.path.dirname(path)   # 获取完整路径中的目录部分
# os.path.basename(path)  # 获取完整路径中的主体部分
# os.path.split(path)     # 将一个完整的路径切割成目录部分和主体部分
# os.path.join(path1, path2)      # 将两个路径合并成一个
# os.path.exists(path)    # 检查某个路径是否真实存在
# os.path.samefile(path1, path2)      # 检查两个路径是否是同一个文件



print(os.path.join('D:\pycharm\\test framework\config', 'config.yml'))