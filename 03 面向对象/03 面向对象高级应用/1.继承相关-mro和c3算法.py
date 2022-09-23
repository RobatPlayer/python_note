# 如果类中有继承关系，可以通过内置函数mro获得
class C:
    pass


class D:
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.mro())  # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
print(A.__mro__)

# mro()内部是c3算法
'''
已知mro(A)=[A]+[B,C]  -->> mro(A)=[A,B,C]
当计算A的继承关系时 mro(A)=[A]+marge(mro[B]+mro[C]+[B,C])  marge是一个函数，左边函数的继承关系加上右边再加上继承的类
mro(A)=[A]+marge([B,object]+[C,object]+[B,C])  
拿第一个参数的第一个元素B与后面的除了第一个元素比较，如果后面没有就提取出来,并且把后面的第一个相同元素剔除，如果有相同的则跳过,下次还从这个元素开始
mro(A)=[A]+[B]+marge(+[C,object]+[C])  
mro(A)=[A]+[B]+[C]+[object]=[A,B,C,objecet]
'''


# 分析上例
# mro(A) = [A] + marge(mro[B] + mro[C] + [B, C])
# mro(A) = [A] + marge([B,D] + mro[C] + [B, C])
# mro(A) = [A] + [B,D,C]-->>[A,B,D,C]

# 一句话搞定继承关系：从左到右，深度优先，大小钻石，留住顶端  钻石指菱形继承

# py2和py3的区别
# py2.2继承是不留顶端的
class Foo:  # 经典类，不继承object，不留顶端
    pass


class Fo(object):  # 新式类，继承object，留顶端
    pass

# 到了py3全部都是新式类
