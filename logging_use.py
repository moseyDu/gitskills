# logging是一个用于记录日志的标准库模块
# 日志等级(依次升高)：
#     --DEBUG：最详细的日志信息，典型应用场景是 问题诊断
#     --INFO：信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
#     --NOTICE
#     --WARNING：当某些不期望的事情发生时记录的信息(如磁盘可用空间较低)，但此时应用程序还是正常运行的
#     --ERROR：由于一个更严重的问题导致某些功能不能正常运行时记录的信息
#     --CRITICAL：当发生严重错误时，导致应用程序不能继续运行时记录的信息
#     --ALERT
#     --EMERGENCY


import logging


# 常用函数：
logging.debug(msg)      # 创建一条严重级别为DEBUG的日志记录

logging.basicConfig(**kwargs)       # 对root logger进行一次性配置
# 该函数可接收关键字参数如下：
#     filename:指定日志输出目标文件的文件名
#     filemode:指定日志文件的打开模式，默认为'a'，该项要在filename指定时才有效
#     format:指定日志格式字符串
#     level:指定日志器的日志级别
#     handlers:创建多个handler的可迭代对象
# filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常


# logging模块的四大组件：
#     --日志器Logger：提供应用程序代码直接使用的接口
#     --处理器Handler：用于将日志记录发送到指定的目的位置
#     --过滤器Filter：提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出(其它的日志记录将会被忽略)
#     --格式器Formatter：用于控制日志信息的最终输出格式























