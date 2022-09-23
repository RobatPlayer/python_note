# 1.如何查看一个值得内存地址？
# 使用id（）

# 2.函数的参数传递的是引用（内存地址）还是值（拷贝一份）？
# 内存地址

# 3.看代码写结果
v1 = {}
v2 = v1
v1["k1"] = 123
print(v1, v2)  # {'k1':123}{'k1':123}


# 4.看代码写结果
def func(k, v, info={}):
    info[k] = v
    return info


v1 = func(1, 2)
print(v1)  # {1:2}

v2 = func(4, 5, {})
print(v2)  # {4:5}

v3 = func(5, 6)
print(v3)  # {1:2,5:6}


# 5.看代码写结果

def func(k, v, info={}):  # info-->1010101  {}
    info[k] = v
    return info


v1 = func(1, 2)  # info-->1010101   {1:2}
v2 = func(4, 5, {})  # info-->1111111  {4:5}
v3 = func(5, 6)  # info--> 1010101  {1:2,5:6}

print(v1, v2, v3)  # {1:2,5:6} {4:5} {1:2,5:6}


# 6.简述第5题、第6题的结果为何结果不同。
# 五六题v1和v3指向的都是系统原有的内存地址，第五题v1在值未改变之前就是打印出来，而在第六题v1在值改变之后才打印输出

# 7.看代码写结果

def func(*args, **kwargs):
    print(args, kwargs)
    return "完毕"


v1 = func(11, 22, 33)
print(v1)  # (11,22,33) {}

v2 = func([11, 22, 33])
print(v2)  # ([11,22,33],) {}

v3 = func(*[11, 22, 33])
print(v3)  # (11,22,33)  {}

v4 = func(k1=123, k2=456)
print(v4)  # ()  {'k1':123,'k2':456}

v5 = func({"k1": 123, "k2": 456})
print(v5)  # ({"k1": 123, "k2": 456})  {}

v6 = func(**{"k1": 123, "k2": 456})
print(v6)  # ()  {"k1": 123, "k2": 456}

v7 = func([11, 22, 33], **{"k1": 123, "k2": 456})
print(v7)  # ([11,22,33],)  {"k1": 123, "k2": 456}

v8 = func(*[11, 22, 33], **{"k1": 123, "k2": 456})
print(v8)  # (11,22,33)   {"k1": 123, "k2": 456}


# 8.看代码写结果

def func(*args, **kwargs):
    prev = "-".join(args)
    data_list = []
    for k, v in kwargs.items():
        item = "{}-{}".format(k, v)
        data_list.append(item)
    content = "*".join(data_list)

    return prev, content


v1 = func("北京", "上海", city="深圳", count=99)
print(v1)  # ('北京-上海','city-深圳*count-99')

v2 = func(*["北京", "上海"], **{"city": "深圳", "count": 99})
print(v2)  # ('北京-上海', 'city-深圳*count-99')

# 9.补充代码，实现获取天气信息并按照指定格式写入到文件中。
# 获取天气信息示例
# import requests
#
# res = requests.get(url="http://www.weather.com.cn/data/ks/101010100.html")
# res.encoding = "utf-8"
# weather_dict = res.json()

#  获取的天气信息是个字典类型，内容如下：
# print(weather_dict)
'''
{
    'weatherinfo': {
        'city': '北京',
        'cityid': '101010100',
        'temp': '18',
        'WD': '东南风',
        'WS': '1级',
        'SD': '17%',
        'WSE': '1',
        'time': '17:05',
        'isRadar': '1',
        'Radar': 'JC_RADAR_AZ9010_JB',
        'njd': '暂无实况',
        'qy': '1011',
        'rain': '0'
    }
}
'''

import requests


def write_file(**kwargs):
    # 将天气信息拼接起来写入文件 
    values = kwargs.get('weatherinfo')  # 根据键获取值
    with open('weather.txt', mode='a', encoding='utf-8') as file:  # 打开文件，追加模式
        for key, value in values.items():  # 获取键和值
            result = '-'.join([key, value])  # 通过-连接键值
            file.write(f'{result},')  # 写入文件
        file.write('\n')  # 写完换行
        print('over!')


def get_weather(code):
    """ 获取天气信息 """
    url = f"http://www.weather.com.cn/data/ks/{code}.html"
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


city_list = [
    {'code': "101020100", 'title': "上海"},
    {'code': "101010100", 'title': "北京"},
]
for i in city_list:
    code = i.get('code')
    result = get_weather(code)
    print(result)
    write_file(**result)



# 10.看代码写结果
def func():
    return 1, 2, 3


val = func()
print(type(val) == tuple)  # True
print(type(val) == list)  # False


# 11.看代码写结果

def func(users, name):
    users.append(name)
    print(users)


result = func(['武沛齐', '李杰'], 'alex')
print(result)  # ['武沛齐', '李杰','alex']   None


# 12.看代码写结果
def func(v1):
    return v1 * 2


def bar(arg):
    return "%s 是什么玩意？" % (arg,)


val = func('你')  # 你你
data = bar(val)
print(data)  # 你你 是什么玩意？


# 13.看代码写结果

def func(v1):
    return v1 * 2


def bar(arg):
    msg = "%s 是什么玩意？" % (arg,)
    print(msg)


val = func('你')
data = bar(val)
print(data)  # 你你 是什么玩意？  None


# 14.看代码写结果
def func():
    data = 2 * 2
    return data


data_list = [func, func, func]
for item in data_list:
    v = item()
    print(v)  # 4换行 4 换行 4


# 15.分析代码，写结果：
def func(handler, **kwargs):
    extra = {
        "code": 123,
        "name": "武沛齐"
    }
    kwargs.update(extra)
    return handler(**kwargs)


def something(**kwargs):
    return len(kwargs)


def killer(**kwargs):
    key_list = []
    for key in kwargs.keys():
        key_list.append(key)
    return key_list


v1 = func(something, k1=123, k2=456)
# v1  -->something({'k1':123,'K2':456,"code": 123,"name": "武沛齐"})
# v1 =4
print(v1)  # 4

v2 = func(killer, **{"name": "武沛齐", "age": 18})
# v2 --> killer({"name": "武沛齐", "age": 18,"code": 123})
# v2--> ['name','age','code']
print(v2)  # ['name','age','code']


# 16.两个结果输出的分别是什么？并简述其原因。

def func():
    return 123


v1 = [func, func, func, func, ]
print(v1)  # 四个函数的列表  因为函数可以作为变量，不运行就是变量

v2 = [func(), func(), func(), func()]
print(v2)  # [123,123,123,123]   函数运行会返回结果

# 17.看代码结果
v1 = '武沛齐'


def func():
    print(v1)


func()  # '武沛齐'
func()  # '武沛齐'

# 18.看代码结果

v1 = '武沛齐'


def func():
    print(v1)


func()  # '武沛齐'
v1 = '老男人'
func()  # '老男人'

# 19.看代码写结果
NUM_LIST = []
SIZE = 18


def f1():
    NUM_LIST.append(8)  # 全局变量可以通过局部函数改变，前提是可变类型
    SIZE = 19  # 不可变类型没有global不能改变


def f2():
    print(NUM_LIST)
    print(SIZE)


f2()  # []  18
f1()
f2()  # [8]  18

# 20.看代码写结果

NUM_LIST = []
SIZE = 18


def f1():
    global NUM_LIST
    global SIZE
    NUM_LIST.append(8)
    SIZE = 19


def f2():
    print(NUM_LIST)
    print(SIZE)


f2()  # []  18
f1()
f2()  # [8]  19

# 21.
