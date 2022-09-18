name = '张三'
age = 18
#  %s
print('我叫%s,今年%s岁' % (name, age))
print('我叫%(name)s' % {'name': '张三'})  # 也可以这样

text = '%s,我下载了90%%了' % '张三'  # 加两个%%不会被看做占位符
print(text)

# .format
'我叫{0},今年{1}十八岁'.format('张三', 18)

# f
f'我叫{name},今年{age}十八岁'
name = 'zhangsan'
print(f"今年{22:#b}岁")
print(f'我叫{name.upper()},今年{age}十八岁')

# 面试题
a = 'zhangsan' and 'lisi'  # 首先会把字符串转化成布尔值，前者为true，则最终结果等于后者的值，如果前者为false则取前者的值
print(a)
# 如果既有and又有or，则先计算and再计算or
b = 0 or 4 and 2 or 0 and 3 or 5
# 0 or 2 or 0 or 5
# 2 or 0 or 5
# 2 or 5
# 2
print(b)

# 加上not，则先计算not   not--> and --> or
