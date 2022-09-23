# 一个函数内部的代码不能被另外一个函数共用
# Python是以函数为作用域的，也就是说一个函数的内部的参数可以一直用
def fun():
    for i in range(5):
        print(i)
    print(i)  # 这个i=4也会被打印出来
    if True:
        value = 'hello'
        print(value)
    print(value)  # 这个value只要上面if的代码执行，这个就不会报错
    # if 1<0:
    #   name = '张'
    #    print(name)
    # print(name)  # 但是如果上面不执行就会报错


fun()

# 函数称为局部作用域

# global关键字
# 在局部作用域中可以修改和读取可变类型的全局变量，无法对全局变量重新赋值。。。但是可以通过global关键字修改
COUNTRY = '中国'
CITY = [11, 22, 33]


def dowload():
    COUNTRY = '上海'  # 默认会在局部作用域重新开辟一个id，不会修改全局变量
    global CITY
    CITY = [1, 2, 3]  # 这样就会把全局变量重新赋值
