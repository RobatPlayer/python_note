# 第1组 数学运算 5个
# 1. 绝对值  abs()
print(abs(-10))

# 2. 取指数 pow()
print(pow(3, 3))

# 3.求和  sum()  里面必须传可以被for循环的参数
print(sum((1, 2)))
print(sum([1, 2, 3, 4]))

# 4.求商和余数   divmod(x,y)
print(divmod(9, 2))

# 5.小数点后保留几位   round(x,y)
print(round(3.1415926, 2))

# 第2组，数据处理
# 6.最小值 min()
print(min([11, 22, 33]))  # 可以传迭代类型
v3 = min([11, 2, -5, -1, 3], key=lambda x: abs(x))  # 也可以这样用，先加工再处理
print(v3)

# 7.最大值 max()

# 8.是否全部为True  all()
print(all([11, 22, 33, '']))
print(all('你好'))

# 9.是否存在True   any()
print(any([11, 22, 33, '']))

# 第3组，进制转换
# 10.bin()

# 11.oct()

# 12.hex()

# 第4组，编码转换
# 13.ord（）

# 14.chr()

# 第5组，类型转化
# 15.int()

# 16.float()

# 17.str()

# 18.bool()

# 19.list()

# 20.dict()

# 21.tuple()

# 22.set()

# 23.bytes()
bytes('张三', encoding='utf-8')  # 相当于 '张三'.encode('utf-8')

# 第6组其他
# 24.len()

# 25.print()

# 26.input()

# 27.open()

# 28.type()

# 29.range()

# 30.enumerate()

# 31.id()

# 32.hash()

# 33.显示python内部提示信息  help()
import random

# help(random)

# 34.zip()  将每个变量的元素从头到尾分别打包
v1 = [11, 22, 33]
v2 = [1, 3, 5, 4]
v3 = ['hello', 'world', 56, 456, '9']
result = zip(v1, v2, v3)
for i in result:
    print(i)

# 35.callable()  判断是否可以执行，即后面是否可以加（）

# 36.sorted() 排序，其他类型也能排序
info = {
    'hello': {
        'id': 10,
        'age': 20
    },
    'my': {
        'id': 12,
        'age': 22
    },
}
data = sorted(info.items(), key=lambda x: x[1]['id'],reverse=True)  # 根据id的值排序，函数返回什么就根据什么排序
print(data)
