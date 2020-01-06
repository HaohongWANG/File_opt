# -*- coding:utf-8 -*-
from openpyxl import load_workbook
import shutil
import os
import tqdm
import json
import numpy as np

#import pig_video_test_change

"""
本文件用于调用华芯提供的接口，读入其生成的json文件，返回未识别信息，并根据正确的猪脸编号，记录未被识别的栏杆位置
"""

def distort_num(json_dir,predict=False):
    # 1.读入xlsx文件
    wb = load_workbook("pig_number_v1127.xlsx")
    sheet = wb.active
    title, pig_num_truth = [],[]
    for cell in sheet["3"]:
        pig_num_truth.append(cell.value)
    
    del(pig_num_truth[0:2]) #删除冗余元素
    pig_num_truth[11] = 66  
    pig_num_truth[16] = 16  #短期修正两个可能错误的编号
    
    #print(np.sort(pig_num_truth))
    print(pig_num_truth)
    #print(len(pig_num_truth))  #测试用代码
    
    # 2.调用华芯接口，生成对应json文件
    if predict == True:
        pig_video_test_change.dealwithvideo()  #此处需要写新接口
    
    # 3.读入json文件
    pig_found = []  #用于保存json文件中已被识别到的猪的编号
    json_list = os.listdir(json_dir)
    for json_file in json_list:
        with open(json_dir+json_file, 'r') as file_in:
            data = json.load(file_in)
        for i in data['pig_face']:
            pig_found.append(int(i['id']))
            #print(i["id"])
        file_in.close()
    pig_found = np.unique(np.sort(pig_found))  
    
    print (pig_found)
    print(len(pig_found))
    
    # 4.核验二者不同之处
    fn = np.setdiff1d(pig_num_truth,pig_found)
    fp = np.setdiff1d(pig_found,pig_num_truth)
    fence = []
    for n in fn:
        index = np.where(pig_num_truth==n)
        fence.append(int(index[0]))
    fence = np.array(fence)+1 
    
    print("存在该猪但未验出：{}".format(fn))
    print("未被建档猪的栏号：{}".format(fence))
    print("不存在该猪但被验出：{}".format(fp))
    print("{}头猪未被识别。\n".format(abs(len(fn)-len(fp))))
    
    #print(type(fp[0]))
    
    # 5.把错误识别的猪从json文件中删除
    for json_file in json_list:
        read_json_file = json_dir + json_file
        write_json_file = json_dir + "new_{}".format(json_file[8:])
        
        with open(read_json_file, 'r') as file_in:
            data = json.load(file_in)
            file_in.close()
        face_list = data['pig_face']
        
        for i in range(len(face_list)-1,-1,-1):
            for k in fp:
                if int(face_list[i]['id']) == k:
                    del(face_list[i])
        
        #print(data)
        with open(write_json_file,'w') as file_out:
            json.dump(data,file_out)
            #print("写入成功！")
            file_out.close()
        
json_dir = "F:/File_opt/test_video_1112/"
    
distort_num(json_dir)    