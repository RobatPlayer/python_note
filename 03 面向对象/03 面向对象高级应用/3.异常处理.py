# try-except
try:
    pass
except:
    pass

# try-except-finally
try:
    pass
except Exception as e:
    print(e)
finally:  # try 中的代码无论报不报错，finally里面的代码都会执行
    pass

# try-except-else
try:
    pass
except:
    pass
else:
    pass  # 只有try中的代码不报错这个才会执行

# 异常细分
"""
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问n x[5]
KeyError 试图访问字典里不存在的键 inf['xx']
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
"""


# 自定义异常
class My_Exception(Exception):
    title = '请求错误'

    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 继承父类
        self.msg = msg


try:
    raise My_Exception('错误')  # 主动抛出异常 ，触发异常
except My_Exception as e:  # e就是上面的类
    print('我的异常被触发了', e.title, e.msg)
except Exception as e:
    print('Exception', e)


# 特殊的finally，可以放在函数里面
def func():
    try:
        name = '杜孝先'
        return
    except Exception as e:
        print(e)
    finally:
        print(666)


func()  # finally里面的代码遇到return还会执行


def func():
    print(666)
    return '成功'


def fun(num):
    try:
        print(num)
        return func()
    except Exception as e:
        print(e)
    finally:
        print(123456)


print(fun(3))  # 首先会执行3 然后再执行返回的func()函数，再最后的return之前执行finally
