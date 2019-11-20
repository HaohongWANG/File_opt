# -*- coding:utf-8 -*-

import cv2
import os
from tqdm import tqdm


def read_img(path):
    videos_list = os.listdir(path)  # 读取文件夹下的所有文件，存入列表
    pic_count = 1  # 帧计数及图像命名

    notMp4List = []
    # 删除非mp4文件
    for file_name in videos_list:
        if not file_name.endswith(".mp4"):
            notMp4List.append(file_name)
            
    for file in notMp4List:
        videos_list.remove(file)
    # print (videos_list)

    channel_name = os.getcwd().split("\\")[-1]  # 获取当前文件夹名称
    img_folder = channel_name + "_img"  # 设定[通道_日期_img]文件夹名称
    
    if not os.path.exists(img_folder):
        # 如果对应img文件夹不存在则创建
        os.makedirs(("./{}".format(img_folder)))  # 创建[通道_日期_img]文件夹

    write_path = "./" + img_folder + "/"

    for i in tqdm(range(len(videos_list))):
        # 针对每个视频进行循环
        cap = cv2.VideoCapture(path + videos_list[i])  # 打开视频文件
        video_open_flag = cap.isOpened()  # 视频是否打开的标记
        video_duration = cap.get(7) # 获取当前视频总帧数
        #print("\nThis video has {} frames.\n".format(video_duration))
        
        if not video_open_flag:
            # 如果视频打开失败则出现以下提示
            print("\n\n*** 视频{}打开失败 ***\n\n".format(videos_list[i]))

        frame_count = 0  # 帧数计数器
        while video_open_flag:

            frame_count = frame_count + 1  # 逐次读取图片中的每一帧
            video_open_flag, frame = cap.read()  # 读入视频
            params = [int(cv2.IMWRITE_JPEG_QUALITY), 50]  # 设定导出图片的格式及质量

            if frame_count % 60 == 0:
                # 每60帧保存一张图像
                cv2.imwrite("{}{}{:0>5d}.jpg".format(write_path, str(videos_list[i][14:18])+'_',pic_count), frame, params)  # 将视频中的帧保存为图像
                pic_count += 1  # 图片计数器+1
                print("当前视频进度：{:0.2f}%\n".format(frame_count/video_duration*100)) # 以百分比形式显示当前视频处理进度

        cap.release()  # 关闭视频文件
        print("第{}个视频 {} 转换完成。".format(i + 1, videos_list[i]))
        print("该视频共有: {}帧，共计导出{}张图片。\n".format(video_duration, video_duration//60))

    print("全部视频转换完成，可以开始标注工作啦~")


read_img("./")
