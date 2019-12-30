# -*- coding:utf-8 -*-

import os
import shutil
"""
将该文件放置在与 1008/ 同级目录下，运行后将:
1. 重命名每一通道下的jpg和xml文件
2. 移动上述文件至同一文件夹 1008/final/ 内
"""
def archive_img(path):
    channel_list = os.listdir(path)
    for channel_dir in channel_list:
        # print(channel_list)
        if channel_dir.startswith("ch"):
            ch_path = "{}{}/".format(path, channel_dir)
            # print(ch_num) # 测试待添加的通道名称是否正确
            # print(ch_path) # 测试待添加的路径名称是否正确
            file_list = os.listdir(ch_path)
            for file in file_list:
                os.rename("{}{}".format(ch_path, file),
                 "{}{}_{}".format(ch_path, channel_dir,file))
    # end for
            file_list = os.listdir(ch_path)
            for file in file_list:
                shutil.move("{}{}".format(ch_path,file),"./1008/")
archive_img("./1008/")
