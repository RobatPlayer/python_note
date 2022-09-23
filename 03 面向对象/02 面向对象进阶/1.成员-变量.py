# 实例变量，归属于变量，只能通过实例对象调用
# 类变量，归属于类，能通过类调用，也能通过实例对象调用
class Person:
    country = '中国'  # 类变量  ，相当于类的全局变量

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'{self.country}-{self.name}-{self.age}')


print(Person.country)
p1 = Person('张三', 28)
p1.show()
p1.sex = '男'  # 在对象p1中新增一个对象sex=男
print(p1.sex)
