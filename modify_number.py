import os
from xml.etree.ElementTree import parse, Element

def modify_pig(wrong_num, right_num, file_name):
    doc = parse(file_name)
    root = doc.getroot()
    #name = root.iter('name')
    #print(name)
    for name in root.iter('name'):
    # name = obj.find('name')
        if int(name.text) == wrong_num:
            name.text = str(right_num)
            print("\n\nInside file: {}, number {} has been modified to {}.\n\n".format(file_name,wrong_num,right_num))
        doc.write(file_name)


def modify(path):
    file_list = os.listdir(path)
    not_XML_list = []
    for file in file_list:
        if not file.endswith(".xml"):
            not_XML_list.append(file)
    for file in not_XML_list:
        file_list.remove(file)
    # print(file_list)
    for file_name in file_list:
        complete_name = "{}{}".format(path,file_name)
        modify_pig(11,66,complete_name)
        
        
modify("Z:/Pig/1025/ch18_1025/ch18_1025_img/")