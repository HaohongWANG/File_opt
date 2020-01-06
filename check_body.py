# -*- coding:utf-8 -*-
from xml.etree.ElementTree import parse, Element
import os
'''
用于统计猪只每部位的标记数量
'''

def count_pig_body_part(path):
    part_dic = {1:0,2:0,3:0,4:0,5:0}
    xml_list = os.listdir(path)
    
    for xml_file in xml_list:
        if xml_file.endswith('xml'):
            doc = parse(path+xml_file)
            root = doc.getroot()
            for name in root.iter('name'):
                try:
                    part_dic[int(name.text)]+=1
                except ValueError:
                    print("文件{}中有标注错误。".format(xml_file))
        # check num in js file.
        #for i in data[]
        #if js.'name' == 0:
        #    part_dic[name] += 1

    # 打印各部位数量
    print(part_dic)
    '''
    for i in part_dic:
        print()
    '''
count_pig_body_part("./")