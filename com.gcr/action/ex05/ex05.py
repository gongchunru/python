#encoding=utf8


# 练习册 5-调整文件夹内所有图片的分辨率


"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

import os
from PIL import Image

IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640


# 改变图片的尺寸大小
def reset_pic_size(file_path, new_path, width=IPHONE5_WIDTH, height=IPHONE5_HEIGHT):
    image = Image.open(file_path)
    image_width, image_height = image.size

    if image_width > width:
        image_height = width * image_height // image_width
        image_width = width
    if image_height > height:
        image_width = height * image_width // image_height
        image_height = height

    new_image = image.resize((image_width, image_height), Image.ANTIALIAS)
    new_image.save(new_path)


# 从文件夹中循环改变每一张图片
def find_and_resize_pic_from_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if file_name.lower().endswith('jpg') or file_name.lower().endswith('png'):
                file_path = os.path.join(root, file_name)
                file_new_path = 'iPhone5_' + file_name
                reset_pic_size(file_path=file_path, new_path=file_new_path)


find_and_resize_pic_from_dir('./')
