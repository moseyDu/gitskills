# PrettyTable库：可用来生成美观的ASCII格式的表格

import prettytable as pt

table = pt.PrettyTable()
# 按行添加数据：
table.field_names = (["name", "sex", "age", "hobby"])
table.add_row(["aa", "girl", 12, "sing"])
table.add_row(["bb", "boy", 14, "play games"])
table.add_row(["cc", "girl", 13, "dance"])

# 按列添加数据：
table.add_column("place", ["hangzhou", "beijing", "shanghai"])


# 使用不同的输出风格：
# table.set_style(pt.MSWORD_FRIENDLY)
# table.set_style(pt.PLAIN_COLUMNS)
# table.set_style(pt.RANDOM)
# table.set_style(pt.DEFAULT)
# print(table)


# # 获取表格字符串：
# s = table.get_string()
# print(s)
#
#
# # 获取指定行：
# s1 = table.get_string(fields=["name", "hobby"], start=1, end=2)
# print(s1)


# 自定义表格输出样式：
# 设定左对齐：
table.align = 'l'

# 设定数字输出格式：
table.float_format = '2.2'

# 设定边框连接符为*号：
table.junction_char = '*'

# 设定排序方式：
table.sortby = "age"

# 设定左侧不填充空白符：
table.left_padding_width = 0

# 不显示边框：
# table.border = 0

# 修改边框分隔符：
table.set_style(pt.DEFAULT)
table.horizontal_char = '+'

# # 输出html代码：
# s2 = table.get_html_string()
# print(s2)

print(table)


























