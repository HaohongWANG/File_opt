# -*- coding:utf-8 -*-
from openpyxl import load_workbook
import shutil
import os
import tqdm
import json
import numpy as np

"""
方法说明：
1. 读入同目录下记录猪脸编号的xlsx文件；
2. 读入测试目录下的预测结果build.json文件；
3. 在控制台输出预测结果与真实结果间的差别；
4. 将修改后结果写入new_build.json文件中；
5. 通过modify标志控制是否删除json文件中的错误预测结果。

更新日志：
2020-01-06修改：
* 改为合并至pig_video_test_change内，由主函数调用本文件
* 改为读入build.json文件而非全部json文件
+ 在输出json文件中添加未被识别的猪栏编号
+ 增加调取表格文件中不同日期信息的功能
- 去除调用华芯接口的部分


2019-12-31创建：
本文件用于调用华芯提供的接口，读入其生成的json文件，返回未识别信息，并根据正确的猪脸编号，记录未被识别的栏杆位置
"""

def change_num(test_video_folder,date="1008-1016",modify=True):
    # 1.读入xlsx文件
    real_data = {"0929":2,"1008-1016":3,"1107":4,"1115":5,"1127":6} # xlsx文件中日期与行号对应关系

    wb = load_workbook("pig_number_v1127.xlsx")
    sheet = wb.active
    title, pig_num_truth = [],[]
    for cell in sheet[real_data[date]]:
        pig_num_truth.append(cell.value)
    
    del(pig_num_truth[0:2]) #删除冗余元素
    pig_num_truth[11] = 66  
    pig_num_truth[16] = 16  #短期修正两个可能错误的编号
    
    #print(pig_num_truth)
    
    # 2.读入json文件
    pig_found = []  #用于保存json文件中已被识别到的猪的编号
    with open(test_video_folder+"/build.json", 'r') as file_in:
        data = json.load(file_in)
    file_in.close()
    for i in data:
        pig_found.append(int(i['id']))
    #print(pig_found)
            
    #pig_found = np.unique(np.sort(pig_found))  
    #print(len(pig_found))
    
    # 3.核验二者不同之处
    fn = np.setdiff1d(pig_num_truth,pig_found)
    fp = np.setdiff1d(pig_found,pig_num_truth)
    fence = []
    for n in fn:
    # 记录未被识别的猪所在栏杆编号
        index = np.where(pig_num_truth==n)
        fence.append(int(index[0]))
    fence = np.array(fence)+1 
    
    print("存在该猪但未验出：{}".format(fn))
    print("未被建档猪的栏号：{}".format(fence))
    print("不存在该猪但被验出：{}".format(fp))
    print("{}头猪未被识别。\n".format(abs(len(fn)-len(fp))))
    
    #print(type(fp[0]))
    
    # 4.把错误识别的猪从json文件中删除
    if modify == True:
        read_json_file = test_video_folder + "/build.json"
        write_json_file = test_video_folder + "/new_build.json"
        
        with open(read_json_file, 'r') as file_in:
            face_list = json.load(file_in)
            file_in.close()
            
        for i in range(len(face_list)-1,-1,-1):
            for k in fp:
                if int(face_list[i]['id']) == k:
                    del(face_list[i])
        
        dic = {"id":"noidentified","success":fence.tolist()}
        face_list.append(dic)
        print(face_list)
        with open(write_json_file,'w') as file_out:
            json.dump(face_list,file_out)
            #print("写入成功！")
            file_out.close()
      
test_video_folder = "./train1"
    
change_num(test_video_folder,date="1008-1016",modify=True)    