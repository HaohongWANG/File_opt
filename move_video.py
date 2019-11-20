import os, shutil

def move_video(path):
    folder_list = os.listdir(path)
    for folder in folder_list:
        video_list = os.listdir("./{}/Download/".format(folder))
        print(video_list)
        for video in video_list:
            shutil.move("./{}/Download/{}".format(folder,video),"./")


move_video("./")