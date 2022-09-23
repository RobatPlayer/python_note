# 1.列表推导式
lst = [i for i in range(10)]
print(lst)
print([i ** 3 for i in range(1, 10, 2)])
print([[i, i] for i in range(10)])
print([[i, i] for i in range(10) if i > 3])  # 如果成立

# 2.集合
print({i for i in range(10)})
print({(i, i) for i in range(10)})

# 3.字典
print({i: 'a' for i in range(10)})

# 4.元组，元组不同于其他类型
data = (((i, i), (i, 'a')) for i in range(10))
print(data)  # 元组会先得到一个生成器
print(next(data))  # 然后可以用next()去取值
print(next(data))
print(next(data))
for i in data:  # 或者去遍历
    print(i)

# 面试题
data = [lambda x: x + i for i in range(10)]  # [函数，函数，函数...]  i=9
v1 = data[0](100)  # 在列表推导式也会围护一个作用域，x+i，i在自己的作用域没找到会在上一级找，即i=9
v2 = data[3](100)
print(v1, v2)

# 嵌套循环
lst = [[i, j] for i in range(10) for j in range(5)]
print(lst)

print([f'{x}x{y}={x * y}' for x in range(1, 10) for y in range(1, x + 1)])

poke_list = [(x, y) for x in ['黑桃', '红桃', '梅花', '方片'] for y in range(1, 14)]
print(poke_list)


# 函数嵌套
def num():
    return [lambda x: x * i for i in range(3)]


result = [m(2) for m in num()]
print(result)


# 首先执行函数  num()  得到返回值  [函数，函数，函数] 此时i=2
# 然后循环上面的列表（返回值）
# 每个元素 函数(2)  函数(2)  函数(2)  =2*2=4
# 最后结果是[4,4,4]

# 如果换成生成器
def num():
    return (lambda x: x * i for i in range(3))


result = [m(2) for m in num()]
print(result)
# 首先会得到一个生成器num()
# 然后第一次调运函数 此时m=函数 i=0 m(2)=2*0
# 依次类推
# 最后结果是[0,2,4]

# 以上就是生成器和函数的区别
