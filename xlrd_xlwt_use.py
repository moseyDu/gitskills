"""Python操作excel主要用到xlrd和xlwt这两个库，xlrd是读excel，xlwt是写excel"""
# coding:utf-8


# # 读取exel-xlrd：
# import xlrd
#
# # # 打开excel并获取所有sheet：
# workbook = xlrd.open_workbook('E:\测试笔记\数据查询\年中活动数据查询.xls', formatting_info=True)
# # print(workbook.sheet_names())
# # print(workbook.sheet_names()[1])
#
#
# # 根据sheet索引或者名称获取sheet的内容、名称、行数、列数(索引从0开始)：
# sheet2 = workbook.sheet_by_index(1)
# # sheet2 = workbook.sheet_by_name('7-23')
# # print(sheet2.name, sheet2.nrows, sheet2.ncols)
#
# # # 获取整行或整列的值(value从0开始)：
# # rows = sheet2.row_values(3)
# # cols = sheet2.col_values(1)
# # print(rows, '\n', cols)
#
#
# # # 获取指定单元格的内容：
# # print(sheet2.cell(0, 0))
# # print(sheet2.row(1)[4])
# # # 获取单元格数据类型(0-empty，1-string类型，2-number，3-date，4-Boolean，5-error)：
# # print(sheet2.cell(1, 4).ctype)
#
# # # 处理日期内容：
# # date = sheet2.cell(1, 4)
# # if date.ctype == 3:
# #     print(xlrd.xldate_as_tuple(date.value, workbook.datemode))
# #     print(xlrd.xldate_as_datetime(date.value, workbook.datemode))
#
#
# # 获取合并单元格的内容(只读取合并区的第一个索引)：
# print(sheet2.cell(9, 1))        # 横向合并
# print(sheet2.cell(9, 0))        # 竖向合并
#
# # 也可以用merged_cells方法进行处理,获取合并单元格的第一个cell的行列索引：
# print(sheet2.merged_cells)
# # merged_cells函数返回值的4个参数表示：(row,row_range,col,col_range),其中[row,row_range),同理[col,col_range),包前不包后
# merge = []
# for (row, row_range, col, col_range) in sheet2.merged_cells:
#     merge.append([row, col])    # 获取row和col的低位索引
# print(merge)
# for index in merge:
#     print(sheet2.cell_value(index[0], index[1]))


# 写入excel-xlwt：
import xlwt


def set_style(name, height, bold=False):
    """设置单元格格式"""
    style = xlwt.XFStyle()      # 初始化样式

    font = xlwt.Font()
    font.name = name    # 字体样式
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font

    return style


def write_excel():
    """写入excel"""
    excel_file = xlwt.Workbook()        # 创建工作簿

    # 创建第一个sheet：
    sheet1 = excel_file.add_sheet('sheet1', cell_overwrite_ok=True)
    row0 = ['业务', '状态', '北京', '上海', '深圳', '状态小计', '合计']
    col0 = ['机票', '船票', '火车票', '汽车票', '其他']
    status = ['预定', '出票', '退票', '业务小计']

    # 生成第一行：
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    # 生成第一列和最后一列(合并4列)：
    i, j = 1, 0
    while i < 4*len(col0) and j < len(col0):
        sheet1.write_merge(i, i+3, 0, 0, col0[j], set_style('Arial', 220, True))
        sheet1.write_merge(i, i+3, 6, 6)    # 最后一列
        i += 4
        j += 1

    # 生成最后一行：
    sheet1.write_merge(21, 21, 0, 1, '合计', set_style('Arial', 220, True))

    # 生成第二列：
    i = 0
    while i < 4*len(col0):
        for j in range(0, len(status)):
            sheet1.write(j+i+1, 1, status[j])
        i += 4

    excel_file.save('write_excel.xls')


if __name__ == '__main__':
    write_excel()

# write_merge(x, x+m, y, y+n, string, style):x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示内容































