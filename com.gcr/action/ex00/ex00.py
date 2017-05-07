#encoding:utf-8
#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

#PIL：Python Imaging Library，Python平台上的图像处理库。PIL功能强大，而且API简单易用

# from PIL import Image, ImageDraw, ImageFont, ImageColor

# def add_num(img):
#     # 创建一个对象
#     draw = ImageDraw.Draw(img)
#     # 创建一饿Font
#     myfont = ImageFont.truetype('C:/windows/fonts/BELL.TTF', size=40)
#
#     fillcolor = ImageColor.colormap.get('red')
#     width, height = img.size
#     draw.text((width-30,0), '1', font=myfont, fill=fillcolor)
#     img.save('result.jpg','jpg')
#     return 0

# todo Mac安装PIL一直失败，先放下这个

# from PIL import Image, ImageDraw, ImageFont

# def write_num_on_img(filePath, num):
#     img = Image.open(filePath)
#     #img.size返回一个原则(with, height)
#     size = img.size
#     draw = ImageDraw.Draw(img)
#     color = (255, 0, 0)
#     ttfont = ImageFont.truetype("C:/windows/fonts/BELL.TTF", size=40)
#     # 关键函数，参数：文字的位置，内容，颜色，字体。
#     draw.text((size[0]-30, 0), str(num), fill=color, font=ttfont)
#     #显示一幅已载入的图像
#     img.show()
#     img.save('changed.jpg')
#
# if __name__ == '__main__':
#     write_num_on_img("test.jpg", 4)

