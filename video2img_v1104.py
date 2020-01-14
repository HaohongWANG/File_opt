# -*- coding:utf-8 -*-

import cv2
import os
from tqdm import tqdm
from glob import glob

"""
2020-01-14更新：
* 使用glob替换listdir以减少代码量
+ 提高方法泛用性，可调整帧数间隔和视频文件后缀名

"""

def video2img(path='./',frame_gap=60,video_type='.mp4'):
    videos_list = glob(path+'*'+video_type) # 读取文件夹下指定类型视频文件，存入列表
    pic_count = 1  # 帧计数及图像命名

    # print (videos_list)

    channel_name = os.getcwd().split("\\")[-1]  # 获取当前文件夹名称
    img_folder = channel_name + "_img"  # 设定[通道_日期_img]文件夹名称
    
    if not os.path.exists(img_folder):
        # 如果对应img文件夹不存在则创建
        os.makedirs(("./{}".format(img_folder)))  # 创建[通道_日期_img]文件夹

    write_path = "./" + img_folder + "/"

    for video in tqdm(videos_list):
        # 针对每个视频进行循环
        cap = cv2.VideoCapture(video)  # 打开视频文件
        video_open_flag = cap.isOpened()  # 视频是否打开的标记
        video_duration = cap.get(7) # 获取当前视频总帧数
        #print("\nThis video has {} frames.\n".format(video_duration))
        
        if not video_open_flag:
            # 如果视频打开失败则出现以下提示
            print("\n\n错误：视频{}打开失败！\n\n".format(video))

        frame_count = 0  # 帧数计数器
        video_name = str(video[14:18])+'_'
        
        while video_open_flag:

            frame_count = frame_count + 1  # 逐次读取图片中的每一帧
            video_open_flag, frame = cap.read()  # 读入视频
            params = [int(cv2.IMWRITE_JPEG_QUALITY), 50]  # 设定导出图片的格式及质量

            if frame_count % frame_gap == 0:
                # 每60帧保存一张图像
                cv2.imwrite("{}{}{:0>5d}.jpg".format(write_path,video_name,pic_count), frame, params)  # 将视频中的帧保存为图像
                pic_count += 1  # 图片计数器+1
                print("当前视频进度：{:0.2f}%\n".format(frame_count/video_duration*100)) # 以百分比形式显示当前视频处理进度

        cap.release()  # 关闭视频文件
        print("视频 {} 转换完成。".format(video))
        print("该视频共有: {}帧，共计导出{}张图片。\n".format(video_duration, video_duration//60))

    print("全部视频转换完成，可以开始标注工作啦~")


video2img("./")
