#  字典  键不重复，可变，在3.6之前无序，3.6之后有序
# 键必须是可哈希的，值可以是任意类型


#  ##独有功能
dic = {'name': '张三', 'age': 12, 'email': '@123.com'}
# 1.根据键获取值，不存在获取None   .get(x)
print(dic.get('name'))

# 2.获取所有的键   .keys()
print(dic.keys())  # dict_keys(['name', 'age', 'email'])  获取的是一个高仿列表，可以直接转换成列表,
# 不转换也能被for循环,也可以直接取用判断
print(list(dic.keys()))
for i in dic.keys():
    print(i)

# 3.获取所有的值   .values()
print(dic.values())  # 高仿列表

# 4.获取所有的键值    .items()
print(dic.items())  # 高仿列表，列表里面键值是元组   dict_items([('name', '张三'), ('age', 12), ('email', '@123.com')])
for i in dic.items():
    print(i)
# 也可以用两个元素遍历拆解
for key, value in dic.items():
    print(key, value)

# 5.设置值   .setdefault()
dic.setdefault('age', 18)

# 6.更改键值对    .update({})   传入一个新字典，如果原字典键存在就替换，不存在就创建新的键值对
dic.update({'name': '李四', 'num': 123})
print(dic)

# 7.移除指定键值对   .pop(key)
dic.pop('num')
print(dic)

# 8.按照顺序移除，从后往前  .popitem()
dic.popitem()
print(dic)

# 练习题
""" 
结合下面的两个变量 header 和 stock_dict实现注意输出股票信息，格式如下：
SH601778，股票名称:中国晶科、当前价:6.29、涨跌额:+1.92。
SH688566，股票名称:吉贝尔、当前价:...
"""
header = ['股票名称', '当前价', '涨跌额']
stock_dict = {
    'SH601778': ['中国晶科', '6.29', '+1.92'],
    'SH688566': ['吉贝尔', '52.66', '+6.96'],
    'SH688268': ['华特气体', '88.80', '+11.72'],
    'SH600734': ['实达集团', '2.60', '+0.24']
}

for keys, values in stock_dict.items():
    lst = []
    for i in range(len(values)):
        text = f'{header[i]}:{values[i]}'
        lst.append(text)
    # print(lst)
    date = '、'.join(lst)
    print(keys + '，' + date + '。')

#  ##公共功能
# 1.求并集(3.9新加入)
# 2.求长度
# 3.是否存在
# 4.04 索引和函数，只能通过键获取值，不能通过序号
# 5.根据键修改值（常用），可以直接通过索引键来修改值，如果字典没有这个键值，则会创建一个键值
header = {'name': '张三', 'age': 12, 'email': '@123.com'}
header['name'] = '李四'
print(header)
# 6.for循环，不写默认循环键
for i in header.values():
    print(i)

# ##类型转化dict()

# ##嵌套

# ##浮点型保留小数   round(a,3)
a = 3.1415926
print(a.__round__(3))
print(round(a, 2))
#精确计算小数
import decimal
decimal.Decimal(0.1)