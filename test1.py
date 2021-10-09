""" 运算相关 https://www.runoob.com/python/python-operators.html """


def entrance(name):
    print("开始", name)

    print("\n算术运算")
    a = 10
    b = 2
    print("1.加", a + b)
    print("2.减", a - b)
    print("3.乘", a * b)
    print("4.除", a / b)
    print("5.取余", a % b)
    print("6.幂", a ** b)  # 指数是幂运算aⁿ(a≠0)中的一个参数，a为底数，n为指数，指数位于底数的右上角，幂运算表示指数个底数相乘。当n是一个正整数，aⁿ表示n个a连乘。当n=0时，aⁿ=1。
    print("7.取整除", a // b)  # 向下取整

    # 比较运算符
    print("\n比较运算")
    if a > b:
        print("a > b")
    else:
        print("a <= b")

    if a != b:
        print("a != b")
    else:
        print("a == b")

    # 赋值运算符
    print("\n赋值运算")
    c = a + b
    print("1.c =", c)
    c += a
    print("2.c =", c)
    c -= a
    print("3.c =", c)
    c *= a
    print("4.c =", c)
    c /= a
    print("5.c =", c)
    c //= a
    print("6.c =", c)
    c = int(c)
    print("7.c =", c)
    c += b
    print("8.c =", c)
    c **= b
    print("9.c =", c)

    # 二进制运算符
    print("\n位运算")
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0

    c = a & b  # 按位与 12 = 0000 1100
    print("1.按位与 =", c)
    c = a | b  # 按位或 61 = 0011 1101
    print("2.按位或 =", c)
    c = a ^ b  # 按位异 49 = 0011 0001
    print("3.按位异 =", c)
    c = ~a  # 按位取反 -61 = 1100 0011
    print("4.按位取反 =", c)
    c = a << 2  # 左移2位，去掉左边两位，尾部补充0 240 = 1111 0000
    print("5.左移2位 =", c)
    c = a >> 2  # 右移2位，去掉右边两位，头部补充0 15 = 0000 1111
    print("6.右移2位 =", c)

    # 逻辑运算符
    print("\n逻辑运算")
    a = 10
    b = 10
    if a == 10 and b == 10:  # 布尔与
        print("1.and", "2个都为true即可")
    else:
        print("1.and", "有一个不为true了")

    if a == 10 or b == 10:  # 布尔或
        print("2.or", "一个为true即可")
    else:
        print("2.or", "有两个都不为true了")

    a = 0  # a=0为false,非0为true.
    if not (a):  # 布尔非 not x, 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
        print("3.not", "如果为true边为false")
    else:
        print("3.not", "如果为false边为true")

    # 成员运算符
    print("\n成员运算")
    a = 10
    b = 10
    c = 2
    list = [1, 2, 3, 4, 5, 6]

    if a in list:
        print("1.a 属于 list ")
    else:
        print("1.a 不属于 list")

    if b not in list:
        print("2.b 不属于 list ")
    else:
        print("2.b 属于 list")

    if c in list:
        print("3.c 属于 list ")
    else:
        print("3.c 不属于 list")

    # 身份运算符 身份运算符用于比较两个对象的存储单元
    print("\n身份运算")
    a = 1
    b = 1
    if a is b:  # x is y, 类似 id(x) == id(y)
        print("1.a 与 b 身份一样")
    else:
        print("3.a 与 b 身份不一样")

    b = a = [1]  # x is not y ， 类似 id(a) != id(b)
    if a is not b:
        print("2.a 与 b 身份不一样")
    else:
        print("2.a 与 b 身份一样")

    a = (1, 2, 3)
    b = (1, 2)
    if a is b:
        print("3.a 与 b 身份一样")
    else:
        print("3.a 与 b 身份不一样")

    a = [1, 2]
    b = [1, 2]
    if a is b:
        print("4.a 与 b 身份一样")
    else:
        print("4.a 与 b 身份不一样")
    # 内存空间、变量值
    # is 与 == 区别：
    # is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
    a = {"a": 1}
    b = {"a": 1}
    if a is b:
        print("5.a 与 b 身份一样")
    else:
        print("5.a 与 b 身份不一样")

    if a == b:
        print("6.a 与 b 身份一样")
    else:
        print("6.a 与 b 身份不一样")
