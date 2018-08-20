# pprint模块提供了打印出任何Python数据结构类和方法

import pprint

data = (
    "this is a string", [1, 2, 3, 4], ("more tuples", 1.0, 2.0, 3.0, 4.0),
    "this is yet another string"
)

pprint.pprint(data)


# 使用方法:
# 返回格式化的对象字符串：
pprint.pformat(object, indent=1, width=80, depth=None)

# 判断对象object的字符串对象是否可读：
pprint.isreadable(object)

# 参数：
# indent——缩进，width——行最大宽度，depth——打印的深度(如果超出指定的深度，其余的用...代替)
# stream——输出流对象，如果stream=None，那么输出流对象默认是sys.stdout












