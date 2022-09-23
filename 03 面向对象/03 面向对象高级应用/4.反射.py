from datetime import datetime


# 反射：以字符串形式去对象中进行成员的修改 依赖内置函数
class Person:
    title = '老冯'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'{self.name}的年龄是{self.age}')


obj = Person('杜孝先', 45)

'''获取对象  getattr(对象,属性)'''
print(getattr(obj, 'name'))  # 相当于obj.name
print(getattr(obj, 'age'))
print(getattr(obj, 'xe', 123))  # 当成员不存在时的默认值，不写会报错

so = getattr(obj, 'show')  # 获取到函数，相当于obj.show
so()
getattr(obj, 'show')()

'''修改成员  setattr(对象,属性，新属性)'''
setattr(obj, 'big', 78)
print(getattr(obj, 'big'))

'''判断对象中是否成员  hasattr(对象,成员名称)'''
print(hasattr(obj, 'jak'))
print(hasattr(obj, 'name'))

'''删除成员  delattr(对象，成员名称)'''
delattr(obj, 'big')
getattr(obj, 'show')()

# 一切皆对象，所以反射可以操作类，模块   只要遇到xx.xx都可以通过getattr()实现
print(getattr(Person, 'title'))

fun = getattr(datetime, 'now')
print(fun())

