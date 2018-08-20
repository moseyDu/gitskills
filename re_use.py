# re模块使用：

import re

# 扫描字符串，寻找的第一个由该正则表达式模式产生匹配的位置，并返回相应的MatchObject实例(任意位置定义一个匹配)：
re.search(pattern, string, flags=0)

# 在字符串的开头的零个或更多字符匹配正则表达式模式:
re.match(pattern, string, flags=0)

# 整个字符串匹配正则表达式模式，则返回一个match对象:
re.match(pattern, string, flags=0)

# 作为一个字符串列表，在字符串中，返回所有非重叠匹配的模式:
re.findall("匹配规则", "要匹配的字符串")
# 以列表形式返回匹配到的字符串

# 返回的字符串与所有非字母数字带有反斜杠:
re.escape(string)

# 清楚正则表达式缓存：
re.purge()















