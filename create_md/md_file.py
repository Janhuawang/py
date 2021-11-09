# 文件建立
import os

class File_tool:
    # 功能名
    __f_n__ = None

    def __init__(self,__f_n__):
        self.__f_n__ = __f_n__

    def exec(self):
        f_n = self.__f_n__
        t_name: str = "template"
        if f_n != "" and f_n != t_name:
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
                t_file = open(os.getcwd() + "/" + t_name + "/" + t_name + "_" + assign + ".dart", mode="r+")
                text: str = t_file.read()
                text: str = text.replace("template_", f_n + "_")

                f_l: list = f_n.split("_")
                f_n_n = ""
                if len(f_l) > 0:
                    for ln in f_l:
                        f_n_n += ln.capitalize()

                text: str = text.replace("Template", f_n_n)
                file.write(text)
                print("已成功创建文件：", file.name)
                t_file.close()
                file.close()
