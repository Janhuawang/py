# 获取功能名字
from test_py.create_md.md_file import File_tool


def get_function_name():
    ok = ""
    f = ""
    while ok != "Y":
        f = input("请输入你的功能命名：")
        print("你的功能名为：", f)
        ok: str = input("Y/N：")
    return f


# 文件建立
ft = File_tool(get_function_name())
ft.exec()

# 内容组成

# 建立
