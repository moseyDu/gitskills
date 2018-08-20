# coding:utf-8
# PIL库包含的模块详解

# 一、Image模块，是PIL吐血处理中最常见的模块，基本功能都包含在里面
# Image模块提供了一个相同名称的类，即image类，用于表示PIL图像


# open():从文件加载图像：
from PIL import Image
from PIL import ImageFilter

im = Image.open("C:\\Users\\admin\Desktop\jizhan\jizhan1.jpg")
# # im.show()
#
# # 保存文件：
# # im.save("C:\\Users\\admin\Desktop\jizhan\jizhan1.png")
#
# # 打印格式信息：
# print(im.format)
# # 打印模式信息(图像的模式通常有L：表示灰度图像，RGB表示真彩色图像，CMYK表示出版图像)：
# print(im.mode)
#
# # # 将当前图像转化为其他模式,可使用参数Dither=控制颜色抖动；Palette=控制调色板的产生；Colors=控制用于调色板的颜色数目：
# # new_im = im.convert('L')
# # print(new_im.mode)
# # new_im.show()
#
# # 打印图像尺寸(按照像素数计算)：
# print(im.size)
#
# # 打印图像的相关信息：
# print(im.info)

# # 使用给定的变量mode和size生成新的图像：
# new_im1 = Image.new('RGB', (128, 128), 'BLUE')
# new_im1.show()

# # 从当前图像拷贝某个区域(box定义了上下左右4个像素的坐标)：
# box = (700, 300, 1000, 700)
# im_copy = im.crop(box)
# im_copy.show()
#
# # 将一张图像粘贴带另一张图像上：
# im.paste(im_copy, (100, 100))
# im.show()


# # 使用滤波器处理图像：
# blu = im.filter(ImageFilter.BLUR)           # 均值滤波
# con = im.filter(ImageFilter.CONTOUR)        # 找轮廓
# edge = im.filter(ImageFilter.FIND_EDGES)    # 边缘检测
# blu.show()
# con.show()
# edge.show()


# # 使用给定的两张图像及透明度，合成一张新的图像(这两张图像要有一样的尺寸和模式)：
# im2 = Image.open("C:\\Users\\admin\Desktop\jizhan\jizhan2.jpg")
# im_all = Image.blend(im, im2, 0.8)      # 第一张图片透明度为1-alpha，第二张图片透明度为alpha
# im_all.show()


# # 旋转图像：
# im_45 = im.rotate(45)
# im_45_1 = im.rotate(45, Image.NEAREST, 1)
# im_45.show()
# im_45_1.show()

#
# # 在给定的文件序列中查找指定的帧：
# im_gif = Image.open("D:\pycharm\mo kuai\dongtu.gif")
# # im_gif.show()       # 默认显示第0帧
# im_gif.seek(9)        # 显示第9帧
# im_gif.show()


# 获取某个像素位置的值：
print(im.getpixel((4, 4)))
# 更改某个像素位置的值：
im.putpixel((100, 100), (0, 0, 0))















