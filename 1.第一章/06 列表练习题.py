# 1. 写代码，有如下列表，按照要求实现每一个功能。
li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
#    - 计算列表的长度并输出
print(len(li))
#    - 列表中追加元素"seven",并输出添加后的列表
li.append('seven')
print(li)
#    - 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表
li.insert(1, "Tony")
print(li)
#    - 请修改列表第2个索引位置的元素为"Kelly",并输出修改后的列表
li[2] = 'Kelly'
print(li)
#    - 请将列表的第3个位置的值改成 "妖怪"，并输出修改后的列表
li[2] = '妖怪'
print(li)
#    - 请将列表 `data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li` 中，并输出添加后的列表
data = [1, "a", 3, 4, "heart"]
for i in data:
    li.append(i)
print(li)
#    - 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。
s = "qwert"
for i in s:
    li.append(i)
print(li)
#    - 请删除列表中的元素"barry",并输出添加后的列表
li.remove('barry')
print(li)
#    - 请删除列表中的第2个元素，并输出删除元素后的列表
li.pop(1)
print(li)
#    - 请删除列表中的第2至第4个元素，并输出删除元素后的列表
li[1:4] = ''
print(li)

# 2. 写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5, "c"]
#    - 通过对li列表的切片形成新的列表 [1,3,2]
print(li[:3])
#    - 通过对li列表的切片形成新的列表 ["a",4,"b"]
print(li[3:6])
#    - 通过对li列表的切片形成新的列表  [1,2,4,5]
print(li[::2])
#    - 通过对li列表的切片形成新的列表 [3,"a","b"]
print(li[1:6:2])
#    - 通过对li列表的切片形成新的列表 [3,"a","b","c"]
print(li[1::2])
#    - 通过对li列表的切片形成新的列表  ["c"]
print(li[-1:-2:-1])
#    - 通过对li列表的切片形成新的列表 ["b","a",3]
print(li[-3::-2])

# 3. 写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#    - 将列表lis中的第2个索引位置的值变成大写，并打印列表。
lis[2] = lis[2].upper()  # 直接打印是不行的，要重新赋值
print(lis)
#    - 将列表中的数字3变成字符串"100"
lis[1] = '100'
lis[3][2][1][1] = '100'
print(lis)
#    - 将列表中的字符串"tt"变成数字 101
lis[3][2][1][0] = 101
print(lis)
#    - 在 "qwe"前面插入字符串："火车头"
lis[3].insert(0, '火车头')
print(lis)

# 4. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如 0 武沛齐 1 景女神2 肖大侠
users = ["武沛齐", "景女神", "肖大侠"]
for i in users:
    print(users.index(i), i, end='')
print()

# 5. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：1 武沛齐 2 景女神3 肖大侠
users = ["武沛齐", "景女神", "肖大侠"]
for i in range(len(users)):
    print(i + 1, users[i], end='')
print()

# 6. 写代码实现以下功能 :如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：0,汽车1,飞机2,火箭
# 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
# goods = ['汽车','飞机','火箭']
# try:
#     index=int(input('请输入索引'))
#     if index in range(0,len(goods)):
#         print(f'您选择的商品是{goods[index]}')
#     else:
#         print('输入错误')
# except:
#     print('输入错误')

# 7. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
l = []
for i in range(0, 51):
    if i % 3 == 0:
        l.append(i)
print(l)

# 8. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：[48,45,42...]
l = []
for i in range(0, 51):
    if i % 3 == 0:
        l.insert(0, i)
print(l)

# 9. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
l = []
for i in li:
    text = i.strip()
    if text.startswith('a'):
        l.append(text)
print(l)

# 10. 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。
data = ["京1231", "冀8899", "京166631", "晋989"]
l = []
for i in data:
    if i.startswith('京'):
        l.append(i)
print(l, len(l))
