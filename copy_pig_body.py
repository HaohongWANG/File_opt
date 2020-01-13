import os
import shutil
"""
2020-01-13创建：
读入源目录，将标记好的猪身部位文件及对应图像复制至目标路径。
"""
def copy_labeled(source, target='./', COPY_DELETE_FLAG=0):
    """
    Args:
        source: The directory which includes all channel folders.
        COPY_DELETE_FLAG: 0 for copy, 1 for delete useless.
    """
    path_list = os.listdir(source)
    not_dir =[]
    for file in path_list:
        if not os.path.isdir(source+file):
            not_dir.append(file)
    for file in not_dir:
        path_list.remove(file)
    
    for channel in path_list:
        xml_path = source + channel + '/pig_body/'
        img_path = source + channel + '/'
        xml_list = os.listdir(xml_path)
        img_list = os.listdir(img_path)
        
        target_dir = target + channel[0:4]
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        
        num_for_save = []
        for xml_file in xml_list:
            # save .xml files' names.
            if xml_file.endswith('.xml'):
                num_for_save.append(xml_file[:-4])

        for img_file in img_list:
            # remove unlabeled .jpg files.
            if img_file.endswith('.jpg') and img_file[:-4] in num_for_save:
                # os.remove(file_name)
                img_source = img_path + img_file
                xml_source = xml_path + img_file[:-4] + ".xml"
                # target = "G:/pig/camera"
                try:
                    shutil.copy(img_source, target_dir)
                    shutil.copy(xml_source, target_dir)
                except IOError as e:
                    print("Unable to copy file. %s" % e)
                print("copy file: {} successfully.".format(img_file))
                
        print("{} copy finished.".format(channel))
    

# WARNING: change the directory below before running the codes.
copy_labeled(source='./',target='F:/pig_body_20200113/')
