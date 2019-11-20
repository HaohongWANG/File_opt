import os


def delete_useless(path='./'):
    """
    Args:
        path: The directory which includes all channel folders.
    """
    path_list = os.listdir(path)
    """
    for i in range(len(path_list)):
        # complete the directory.
        path_list[i] = path + path_list[i] + '/'
    """
    for dr in path_list:
        num_for_save = []
        # file_list = os.listdir(dr)
        for file_name in path_list:
            # save .xml files' names.
            if file_name.endswith('.xml'):
                num_for_save.append(file_name[:-4])

        for file_name in path_list:
            # remove unlabeled .jpg files.
            if file_name.endswith('.jpg') and file_name[:-4] not in num_for_save:
                os.remove(file_name)
                print("remove file: {} successfully.".format(file_name))


# WARNING: change the directory below before running the codes.
delete_useless()
