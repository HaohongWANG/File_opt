import os


def make_dir(date='1107'):

    for i in range (16, 27, 1):
        if not os.path.exists("ch{}_{}".format(i,date)):
            os.mkdir ("ch{}_{}".format(i,date))
    os.mkdir("ch43_{}".format(date))


make_dir('1107')