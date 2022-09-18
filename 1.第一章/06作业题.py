# 1. 以下哪些数据类型转换为布尔值为False
# 1  True
# ""   False
# -19  True
# []   False
# [11, 22]   True
# (1)   True
# (1, 2, 3)  True
# ()   False

# 2.运算符操作
v1 = [] or "alex"  # alex
v2 = [11, 22] and (1, 2,)  # (1, 2,)
print(v2)

# 3.比较abc的区别   a=b   c是列表里面加元组
a = [1, 2, 3]
b = [(1), (2), (3)]
c = [(1,), (2,), (3,)]

# 4.将字符串text = "wupeiqi|alex|eric" 根据 ` | ` 分割为列表，然后列表转换为元组类型。
text = "wupeiqi|alex|eric"
print(tuple(text.split('|')))

# 5.根据如下规则创建一副扑克牌（排除大小王）。花色列表:color_list = ["红桃", "黑桃", "方片", "梅花"]
# 牌值 num_list = []
# for num in range(1, 14):
#     num_list.append(num)
# result = []
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]

color_list = ["黑桃", "红桃", "梅花", "方片"]
num_list = []
for i in range(1, 14):
    num_list.append(i)
result = []
for color in color_list:
    for num in num_list:
        result.append((color, num,))
print(result)
