# 定义匿名函数
# lambda 参数：函数体
# lambda x:函数体
# lambda *args,**kwargs : x+100  函数体只能支持一行代码
# 返回值默认是计算结果 ，很适用于简单函数
fun = lambda a1, a2: a1 + a2 + 100
print(fun(10, 20))
func = lambda data: data.replace('苍老师', '**')
funa = lambda data: data.replace('.')[-1]

# ##三元运算
# num = input('内容')
# data = '哈哈哈' if '苍老师' in num else '正经'  # 相当于条件成立取if前面的值，不成立去后面的值
# print(data)

funb = lambda x: '大了' if x > 66 else '小了'
print(funb(1))
