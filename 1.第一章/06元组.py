# (tuple)  不可变 ，   建议在元组的最后加一个逗号
# 比较 (1)  1   (1,)区别

# 独有功能
# 1.相加
# 2.相乘
# 3.获取长度
# 4.04 索引和函数
# 5.切片
# 6.步长
# 7.for 循环    字符串 列表  元组可以被遍历

# ##元组转换 tuple()

# ##嵌套
# 创建用户
l = []
while True:
    name = input('请输入姓名：')
    num = input('请输入号码')
    l.append((name, num,))
    order = input('是否继续？y/n')
    order = order.lower()
    if order == 'y':
        continue
    else:
        break
print(l)
# 用户登录
name = input('请输入姓名：')
num = input('请输入号码')
if (name, num) in l:
    print('登录成功')
else:
    print('登录失败，用户不存在')
