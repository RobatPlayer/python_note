# # 第二阶段考试题
import os
import sys
import time
import functools

# 1.一个大小为100G的文件etl_log.txt，要读取文件中的内容，写出具体过程代码。
# 如果文件有多行
with open('etl_log.txt', mode='r', encoding='utf-8') as file:
    for i in file:
        print(i)

# 如果文件只有一行
file_size = os.path.getsize('etl_log.txt')  # 用于读取文件大小
read_size = 0
with open('etl_log.txt', mode='rb') as file:  # 模式要改成rb
    while read_size < file_size:
        data = file.read()  # 读取字节
        read_size += len(data)  # 加到已读字节中


def fun():
    with open('etl_log.txt', mode='r', encoding='utf-8') as file:
        for i in file.readlines():
            yield i


message = fun()

for i in message:
    print(i.strip())


# 2.编写一个函数，这个函数接受一个文件夹名称作为参数，寻找文件夹中所有文件的路径并输入（包含嵌套）。


def search(folder):
    for path, sol, name_lst in os.walk(folder):
        for name in name_lst:
            file_path = os.path.join(path, name)
            print(file_path)


search('G:\路飞\第二章')


# 3.以下的代码数据的结果是什么？
def extend_list(val, data=[]):
    data.append(val)
    return data


list1 = extend_list(10)  # [10]
list2 = extend_list(123, [])  # [123]
list3 = extend_list("a")  # [10,'a']

print(list1, list2, list3)
# [10,'a'],[123],[10,'a']

# 4.python代码获取命令行参数。
print(sys.argv)

# 5.简述深浅拷贝？
# 深浅拷贝都是说的可变类型，浅拷贝只会拷贝可变类型的第一层，而不会拷贝内部元素，深拷贝会将外层和里层都拷贝一份；
# 不过对于元组来说，浅拷贝始终都不会被拷贝，如果元组里面有可变类型的元素，那么就会被深拷贝拷贝

# 6.基于推导式一行代码生成1 - 100以内的偶数列表。
print([i for i in range(1, 101) if i % 2 == 0])


# 7.请把以下函数转化为python lambda匿名函数
def add(x, y):
    return x + y


add = lambda x, y: x + y


# 8.看代码写结果

def num():
    return [lambda x: i * x for i in range(4)]


# def fun(x):
#     for i in range(4):
#         i * x


result = [m(2) for m in num()]  # num()=[fun,fun,fun,fun]
print(result)  # [6,6,6,6]


# 9.列表推导式和生成器表达式[i % 2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？
# [0,1,0,1,0,1,0,1,0,1]   第二个是一个迭代器

# 10.写装饰器。写timer装饰器实现：计算fun函数执行时间，并将结果给 result，最终打印（不必使用datetime,使用time.time即可）。
def timer(var):
    @functools.wraps(var)
    def inner(*args, **kwargs):
        start = time.time()
        res = var(*args, **kwargs)
        end = time.time()
        return f'耗时{end - start}'

    return inner


@timer
def func():
    pass


result = func()
print(result)

# 11.re的match和search区别？
# match会从字符串起始位置开始匹配，只有从起始位置就符合规则的内容才会被匹配
# search会从字符串起始位置开始匹配，匹配遇到符合规则的第一个内容

# 12.什么是正则的贪婪匹配？或正则匹配中的贪婪模式与非贪婪模式的区别？
# .+ 贪婪匹配会尽可能多的往后匹配，非贪婪模式会尽可能少的进行匹配

# 13.sys.path.append("/root/mods")的作用？、
# 将/root/mods这个文件夹加入到Python内部寻找模块的位置中

# 14.写函数
# 有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
DATA = {
    "time": "2016-08-05T13:13:05",
    "some_id": "ID1234",
    "grp1": {"fld1": 1, "fld2": 2, },
    "xxx2": {"fld3": 0, "fld4": 0.4, },
    "fld6": 11,
    "fld7": 7,
    "fld46": 8
}

# fields: 由"|"连接的以fld开头的字符串, 如fld2 | fld7 | fld29
fields = 'fld7 | fld2 | fld29| fld46| fld1'


def select(fields):
    dic = {}
    for i in fields.split('|'):
        for key, value in DATA.items():
            if i.strip() == key:
                dic.update({i.strip(): value})
            if type(value) == dict:
                if i.strip() in value.keys():
                    dic.update({i.strip(): value.get(i.strip())})
    return dic


print(select(fields))


# 15.编写函数，实现base62encode加密（62进制），例如：
# 内部维护的数据有：0123456789AB..Zab..z(10个数字 + 26个大写字母 + 26个小写字母)。
# 当执行函数：
# base62encode(1)，获取的返回值为1
# base62encode(61)，获取的返回值为z
# base62encode(62)，获取的返回值为10


def base62encode(num):
    pass


print()
# 16.基于列表推导式一行实现输出9 * 9乘法表。
print('\n'.join([' '.join([f'{x}*{y}={x * y}' for x in range(1, 10) for y in range(1, x + 1)])]))
#
lst = []
for i in range(10):
    lst.append(i)
for i in range(26):
    lst.append(chr(i + ord('A')))
for i in range(26):
    lst.append(chr(i + ord('a')))
print(lst)  # 获取到62进制


def base62encode(num):
    consult = divmod(num, 62)[0]
    remainder = divmod(num, 62)[1]
    if consult < 62:
        result = ''.join([str(consult), str(lst[remainder])])
    else:
        con = divmod(consult, 62)
        result = ''.join([str(con[0]), str(con[1]), str(lst[remainder])])

    return result


print(base62encode(4545664))
import string
import itertools

# 生成对应关系,获取0-9 a-z，A-Z
lst = []
print(string.digits, string.ascii_lowercase, string.ascii_uppercase)
# itertools.chain 会将后面的对象生成一个链，逐个遍历
for i in itertools.chain(string.digits, string.ascii_lowercase, string.ascii_uppercase):
    lst.append(i)
print(lst)


def base62encode(num):
    total_count = len(lst)  # 这个是判断进位的对应关系
    position = []  # 这个是用来存放每位的数字
    while num >= total_count:  # 先判断是否大于62
        num, remainder = divmod(num, total_count)
        position.insert(0, lst[remainder])
    position.insert(0, lst[num])
    result = ''.join(position)
    return result


print(base62encode(123))

# print('\n'.join([' '.join([f'{x}*{y}={x * y}' for x in range(1, 10) for y in range(1, x + 1)])]))
# print("\n".join([" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]))

# 第一步
v1 = [[] for i in range(1, 10)]  # [[], [], [], [], [], [], [], [], []] 这样会生成九个列表
print(v1)
# 第二步让九个列表分别写上相应的字符串
v2 = [[f'{i}*{j}={i * j}' for j in range(1, i + 1)] for i in range(1, 10)]
print(v2)
# 第三步，让每个列表里面的元素拼接，变成一个字符串
v3 = [' '.join([f'{i}*{j}={i * j}' for j in range(1, i + 1)]) for i in range(1, 10)]
print(v3)
# 第四步，列表的每个元素换行输出，并去列表
v4 = '\n'.join([' '.join([f'{i}*{j}={i * j}' for j in range(1, i + 1)]) for i in range(1, 10)])
print(v4)

# 总结
print('\n'.join([' '.join([f'{i}*{j}={i * j}' for j in range(1, i + 1)]) for i in range(1, 10)]))
