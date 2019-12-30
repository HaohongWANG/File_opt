import os, shutil

def move_video(path):
    print(path)
    folder_list = os.listdir(path)
    for folder in folder_list:
        video_list = os.listdir("{}{}/Download/".format(path,folder))
        print(video_list)
        for video in video_list:
            shutil.move("{}{}/Download/{}".format(path,folder,video),path)


dir_list = os.listdir("./")
#print(dir_list)
for dir in dir_list:
    if os.path.isdir("./{}".format(dir)):
        dir_name = "./{}/".format(dir)
        #print(dir_name)
        move_video(dir_name)