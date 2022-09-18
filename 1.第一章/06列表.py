# ##独有功能
# 1.单独追加   l.append(x)
l = [123, 456, '我的世界']  # 不会产生新的列表
l.append('hello')
print(l)
'''
names = []
print('欢迎来到NB游戏'.center(20, '-'))
while True:
    try:
        num = int(input('请输入游戏人数'))
        for i in range(num):
            name = input(f'请输入玩家姓名（{i + 1}/{num}）:')
            names.append(name)
        print(names)
        break
    except:
        print('输入错误，请输入整数')
        continue
'''
# 2. 批量增加   .extend(x)
l = [123, 456, '我的世界']
names = ['张三', '李四', 'asad']
l.extend(names)
print(l)

# 3.在指定位置插入    .insert(1,x)
l.insert(1, '马云')
print(l)

# 4.删除   .remove(value)   会报错
l.remove('张三')
print(l)
# 随机抽奖
import random

while l:
    ran = random.choice(l)
    print(f'恭喜抽中{ran}')
    l.remove(ran)

# 5.剔除,根据索引位置删除   .pop(04 索引和函数)
lst = [123, '马云', 456, '我的世界', '张三', '李四', 'asad']
lst.pop(1)
print(lst)
lst.pop()  # 不写会默认删除最后一个
print(lst)
print(lst.pop(2))  # 可以直接输出剔除的值

# 6.清空列表   .clear()
lst.clear()
print(lst)

# 7.根据值获得索引值,不存在会报错     .index(value)
ll = [123, 456, '我的世界', '张三', '李四', 'asad']
print(ll.index('我的世界'))

# 8.列表元素排序   .sort()
lll = [123, 456, 45, 2, 33, -312, -4]
lll.sort()
print(lll)
lll.sort(reverse=True)  # 加关键字可以倒序
print(lll)
ll = ['我的世界', '张三', '李四', 'asad']  # 字符串也可以排序，但是既有整数又有字符串不写
ll.sort()
print(ll)
# 原理：将字符串转换成unicode编码再排序   ord()
date = []
for i in '我的世界':
    date.append(ord(i))
print(date)

# 9.反转原列表      .reverse()
ll = ['我的世界', '张三', '李四', 'asad']
ll.reverse()
print(ll)

# ##公共功能
# 1.相加
# 2.相乘，和字符串类似
# 3.in/not in判断元素是否在列表，但是通过in或者not in判断是否在列表效率很低
# 4.获取长度  len()
print(len(ll))
# 5.04 索引和函数,可以读也可以修改
print(ll[1])
# 6.切片，切片会形成一个新的列表
# 7.步长
# 8.for循环

# 千万不要在循环的过程中，边循环获取列表的数据边删除列表的数据
# 错误示范，因为每次删除列表的索引都会变，但是i的值不会变
lst = ['张三', '李四', '张晓明', '张黎明', '张力']
for i in lst:
    if i.startswith('张'):
        lst.remove(i)
print(lst)

# 正确做法：应该倒着删除,这样索引变成5,4,3,2,1不会影响操作
lst = ['张三', '李四', '张晓明', '张黎明', '张力']
for i in range(len(lst) - 1, -1, -1):
    if lst[i].startswith('张'):
        lst.remove(lst[i])
print(lst)

# ##类型转化  list(x)   将其他类型转换成列表，比如元组，集合
print(list((11, 22, 33, 44)))

# ##嵌套，列表里面在套列表
# 创建列表用户
l = []
while True:
    name = input('请输入姓名：')
    num = int(input('请输入学号：'))
    l1 = [name, num]
    l.append(l1)
    order = input('是否继续输入？y/n')
    if order.upper() == 'Y':
        continue
    else:
        break
print(l)
