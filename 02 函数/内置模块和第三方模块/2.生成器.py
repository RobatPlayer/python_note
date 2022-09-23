# 如果在函数最后写yield，那么函数将不再是函数，称为函数生成器
def fun():
    print(123)
    yield 1
    print(456)  # yield 很像return  会返回值
    yield 2
    print(999)


v = fun()  # 执行函数生成器，函数体默认不会被执行  ,默认返回的是一个生成器对象
print(v)  # <generator object func at 0x000002767732C4A0>

print(next(v))  # 使用next里面放生成器对象，将会执行里面的代码

# yield会记录上一次返回的位置，并在下次执行时从上一次返回处开始
print(next(v))

# next(v)   如果最后遇到 return None 程序会报错  StopIteration

data = fun()  # 获取生成器对象
for i in data:
    # 会自动执行next(data)
    print(i)  # 在for循环中，最后没有yield也不会报错

# 获取300w随机四位数验证码,使用函数生成器可以边使用边生成
import random


def randow_num(num):
    i = 0
    while i <= num:
        yield random.randint(1000, 9999)
        i += 1


data = randow_num(3000000)
next(data)


def decor():
    print(111)
    v1 = yield  # 也可以给yield添加变量
    print(v1)

    print(222)
    v2 = yield
    print(v2)


data = decor()
print(data.send(None))  # 第一次必须传空值  ，还要使用.send()
print(data.send(666))  # 相当于666赋值给v1
