#                  第一阶段考试题                   #
# 1.简述解释型语言和编译型语言的区别。
# 解释型语言变边写边翻译，编译型语言是写完在翻译

# 2.罗列你听说过的编程语言。
# Python，Java，C,C++

# 3.简述位和字节的关系？
# 1字节(b)=8位(bit)

# 4.简述你理解的ascii、unicode、utf - 8、gbk编码。
# ascii是最早的编码格式包含部分文字和数字
# Unicode将一个用文字四个字节表示，
# utf-8包含了世界上几乎所有的语言文字
# gbk是主要是国内编码语言文字

# 5.py2和py3默认解释器编码分别是什么？如何在代码中修改解释器的编码？
# ascii和utf-8，点下面utf-8选项改

# 6.pass的作用？
# 保证Python语法上的正确性，程序不会报错

# 7.is和 == 的区别？
# is比较的是对象的内存地址，==比较的是对象的值

# 8.列举你了解的Python2和Python3的区别。
# 字典获取的键或值py2是列表，py3是高级列表；
# py2的字典无序，py3有序
# 整型和长整型
# 地板除


# 9.变量名的命名规范有哪些？
# 由字母数字下划线组成，开头不能是数字，不能使用Python自带函数的名字

# 10.都有那些值转换为布尔值时为False？
lst = [0, '', tuple(), [], {}, set(), None, ]

# 11.简述如下三个变量的区别。
v1 = (1)
v2 = (1,)
v3 = 1
# v1等于v3，都是字符串类型，v2是元组类型

# 12.你所学的数据类型中哪些是可变的类型？
# 列表，字典，集合

# 13.你所学的数据类型中哪些是可哈希的类型？
# 字符串，整型，元组，布尔，浮点

# 14.你所学的数据类型中哪些是有序的？
# 字符串，列表，字典(3.9) ,元组

# 15.列举你能记得的如下数据类型的方法（独有功能）。
# - str  .upper()大写  .lower()小写  .strip()去除两端的内容(空格)  .splist()按x分割，结果是列表  .center()对齐
#        .zfill()填充0
# - list  .append()    .remove()   .insert()   .replace()
# - dict  .add()   .(key)  .(value)  .item()

# 16.请将字符`name = "wupeiqi"翻转。
name = "wupeiqi"
print(name[::-1])

# 17.进制之间如何进行转换？
print(bin(10))  # 二进制
print(oct(10))  # 八进制
print(hex(10))  # 十六进制
print(int('0b01010101010', base=2))

# 18.循环过程中break和continue的作用是什么？
# break会直接打断循环，并且退出循环；continue会结果本次循环，开始下一轮循环

# 19.看代码写结果
# v1 = 1 or 9 and 88 or [11, 22] and (1, 2, 3)
# 1 or 88 or (1,2,3)
# 1
# v2 = 1 > 5 or "alex" and {"K1": "v1"} or 888
# False or {"K1": "v1"} or 888
# {"K1": "v1"}
# print(v1, v2)
print('---------------------------------------------------')

# 20.看代码写结果
info = [
    {'k1': (1), 'k2': {'k9': 'luffy', 'k10': '武沛齐'}},
    (11, 22, 33, 44),
    {199, 2, 3, 4, 5},
    True,
    ['李杰', 'alex', {'extra': ("alex", [18, 20], 'eric')}]
]
# 利用索引获取 "luffy",44
print(info[0]['k2']['k9'])
print(info[1][-1])
# 删除k10对应的键值对
del info[0]['k2']['k10']
print(info)
# 在{'extra': ("alex", [18, 20], 'eric')}字典中添加一个键值对"name": "武沛齐"
info[-1][-1]['name'] = '武沛齐'
print(info)
# 在集合 {199, 2, 3, 4, 5} 中添加一个"北京"
info[2].add('北京')
print(info)
# 将列表中的True修改为"真"
info[3] = '真'
print(info)
# 在列表 [18, 20] 的第0个索引位置插入 666
info[-1][-1]['extra'][1].insert(0, 666)
print(info)

print('----------------------------------------')
# 21. 判断下面的代码是否正确？正确的话则写出结果，否则标明错误。
# v1 = (11, 22, 33)    (11, 22, 33)
# v2 = (11)             11
# v3 = {11, 2, 33}     {11, 2, 33}
# v4 = {11, 2, ("alex", "eric"), 33}       {11, 2, ("alex", "eric"), 33}
# v5 = {11, 2, ("alex", {"北京", "上海"}, "eric"), 33}   集合里面不能再有集合

# 22.看代码写结果
# v1 = [11, 22, 33]
# v2 = [11, 22, 33]
# v1.append(666)
# print(v1)    [11,22,33,666]
# print(v2)    [11,22,33]

# 23.看代码写结果
l1 = [11, 22, 33]
l2 = l1
l1.append(666)
print(l1)  # [11, 22, 33, 666]
print(l2)  # [11, 22, 33, 666]

# 24.看代码写结果
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)   [1,2,3,4,5]
# print(v2)   [ [111,2222,3,4,5] ,  [111,222,3,4,5] , [1111,2222,3,4,5] ]

# 25.写代码实现，循环提示用户输入内容（Q或q终止），并将内容用"_"连接起来。
# l = []
# while True:
#     content = input('请输入内容（Q或q终止）:')
#     if content.lower() == 'q':
#         break
#     else:
#         l.append(content)
# print('_'.join(l))

# 26.写代码实现，将IP转换为整数。再将以上二进制拼接起来，然后再进行一次翻转。最终将翻转之后的二进制转换为整型。
'''
l = []
while True:
    ip = input('请输入整数（Q或q终止）:')
    if ip.lower() == 'q':
        break
    else:
        ip = int(ip)
        bin_ip = bin(ip)[2:].zfill(8)
        l.append(bin_ip)
print(l)
bin_num = ''.join(l)
print(bin_num)
last_num = int(bin_num[::-1], base=2)
print(last_num)
print('-----------------------------------------------')
'''

# 27.写代码实现，车牌的区域划分。
car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']
# 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}
info = {}
for i in car_list:
    name = i[:2]
    num = i[2:]
    info.update({name: num})
print(info)
print('---------------------------------------')

# 28.写代码实现，数据格式化处理。
text = """id,name,age,phone,job
     1,alex,22,13651054608,IT
     2,wusir,23,13304320533,Tearcher
     3,老男孩,18,1333235322,IT"""
#    info = [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},.... ..]
info = []
text = text.split('\n')
print(text)
title = text.pop(0)
title = title.split(',')
print(title)  # ['id', 'name', 'age', 'phone', 'job']
print(text)
for i in range(len(text)):  # i=0  i=1
    content = text[i].strip().split(',')
    print(content)  # ['1', 'alex', '22', '13651054608', 'IT']
    d = {}
    for x in range(len(title)):  # x=0 1
        d[title[x]] = content[x]  # id:1 name:alex ....
    info.append(d)
print(info)

# 29.写代码实现累乘计算器。
'''
content = input("请输入内容:")  # 用户可能输入 5*9*99.... 或 5* 9 * 10 * 99 或 5 * 9 * 99...
num_list = content.split('*')
product = 1
for i in num_list:
    i = int(i.strip())
    product *= i
print(product)
'''

# 30.使用for循环实现输出九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{x}*{y}={y * x}', end=' ')
    print()

# 31.补充代码实现《棋牌游戏11点》需求：生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示)3个玩家
# 发牌规则默认先给用户发一张牌，其中J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
# 用户根据自己的情况判断是否继续要牌。要，则再给他发一张。不要，则开始给下个玩家发牌。
# 如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌 最终计算并获得每个玩家的分值，

import random

result = {}
user_list = ["alex", "武沛齐", "李路飞"]
# 生成扑克牌
poke_list = []
color = ['黑桃', '红桃', '梅花', '方片']
for x in color:
    for i in range(1, 14):
        poke_list.append((x, i))
poke_list.append(('小王', 14))
poke_list.append(('大王', 15))
print(poke_list, len(poke_list))
a = poke_list
# 随机抽牌，规定分数
for i in user_list:
    print(f'第{user_list.index(i) + 1}位玩家：{i}')
    poke_list = a
    score = 0
    while True:
        index = random.randint(0, len(poke_list) - 1)  # 前后都包括
        if poke_list[index][1] < 11:
            score = score + poke_list[index][1]
        else:
            score = score + 0.5  # 规定分数
        print(poke_list[index])  # 抽到的牌
        poke_list.pop(index)  # 剔除这张牌
        if score > 11:  # 判断爆没爆
            print(f'{score}超过了11，爆掉了')
            print(f'{i}的总分数是：0')
            score = 0
            break
        print(score)  # 展示分数
        ques = input('是否继续要牌？y/n')
        if ques == 'n':  # 判断是否继续要牌
            print(f'{i}的总分数是：{score}')
            break
        else:
            continue
    result.update({i: score})
print('最终结果如下')
print(result)
