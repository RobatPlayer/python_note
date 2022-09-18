# 1.根据需求写代码
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic.update({'k4': 'v4'})
print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1'] = 'alex'
print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
dic["k3"].append(44)
print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(0, 18)
print(dic)

# 2.根据需求写代码
dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}
# 1，将name对应的列表追加⼀个元素’wusir’。
dic1['name'].append('wusir')
print(dic1)
# 2，将name对应的列表中的alex全变成大写。
dic1['name'][0] = dic1['name'][0].upper()
print(dic1)
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
dic1['oldboy'].update({'⽼男孩': 'linux'})
print(dic1)
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
del dic1['oldboy']['alex'][1]
print(dic1)

# 3.循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）
# 例如：用户输入x1 | wupeiqi, 则需要再字典中添加键值对
# d = {}
# while True:
#     text = input('请输入内容，用|隔开,输入q退出')
#     if text.upper() == 'Q':
#         break
#     else:
#         text = text.split('|')
#         d.update({text[0]: text[1]})
# print(d)

# 4.判断以下值那个能做字典的key ？那个能做集合的元素？
# 1     key    元素
# -1    key    元素
# ""    key    元素
# None    key    元素
# [1, 2]
# 1,)    key    元素
# {11, 22, 33, 4}
# {'name': 'wupeiq', 'age': 18}

# 5.将字典的键和值分别追加到key_list和value_list两个列表中，如：
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for keys, values in info.items():
    key_list.append(keys)
    value_list.append(values)
print(key_list)
print(value_list)

# 6.字典
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# a.请循环输出所有的key
for i in dic.keys():
    print(i)
# b.请循环输出所有的value
for i in dic.values():
    print(i)
# c.请循环输出所有的key和value
for i in dic.items():
    print(i)

# 7.请循环打印k2对应的值中的每个元素。
info = {
    'k1': 'v1',
    'k2': [('alex'), ('wupeiqi'), ('oldboy')]
}
for i in info['k2']:
    print(i)

# 8.将字符串处理成字典
d = {}
s = "k: 1|k1:2|k2:3  |k3 :4"
s = s.split('|')
for i in s:
    i = i.replace(' ', '')
    # print(i)
    i = i.split(':')
    # print(i)
    d.update({i[0]: int(i[1])})
print(d)

# 9.写代码,有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
result = {'k1': [], 'k2': []}
for i in li:
    if i < 66:
        result['k1'].append(i)
    elif i > 66:
        result['k2'].append(i)
print(result)

# 10.输出商品列表，用户输入序号，显示用户选中的商品
# 商品列表：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
# 要求:1：页面显示 序号 + 商品名称 + 商品价格，如：1 电脑 1999 .2 鼠标 10
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
'''
l = []
for i in goods:  # {"name": "电脑", "price": 1999}
    name = i['name']
    money = i['price']
    l.append((name, money))
    num = goods.index(i)
    print(num + 1, name, money, end=' ')
print()
print(l)
while True:
    try:
        num = input('请输入商品序号(输入Q/q退出):')
        num = num.lower()
        if num == 'q':
            break
        elif num.isdecimal():
            if int(num) in range(1, 5):
                for i in l[int(num) - 1]:
                    print(i, end='  ')
                print()
        else:
            print('输入错误')
    except:
        print('输入格式错误')
'''
###初级程序员才会这么写
#  ##编写代码的准则：
#  1.尽可能的少if嵌套
#  2.简单的逻辑先处理

a = ['id', 'name', 'age', 'phone', 'job']
b = ['1', 'alex', '22', '13651054608', 'IT']
d = {}
for i in range(len(a)):
    d.update({a[i]: b[i]})
print(d)
