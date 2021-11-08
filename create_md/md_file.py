# 文件建立
import os


def w(f_n):
    if f_n != "":
        f_dir = os.getcwd() + "/" + f_n
        if not os.path.exists(f_dir):
            os.mkdir(f_dir)

        dir_o: list = os.listdir(f_dir)
        if len(dir_o) > 0:
            for n_o in dir_o:
                os.remove(f_dir + "/" + n_o)

        file_list = ["page", "m", "v", "p", "state"]
        for assign in file_list:
            file = open(f_dir + "/" + f_n + "_" + assign + ".dart", mode="w+")
            print("已成功创建文件：", file.name)
            file.close()
