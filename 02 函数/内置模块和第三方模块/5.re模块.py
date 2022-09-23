import re

text = '你好adkj156lqabcbad4545kwcwkjajkfas'
# 1.re.findall()

# 2.re.match()  从起始位置开始匹配，匹配成功返回一个对象，否则返回None  ，必须最开始就符合规则
print(re.match('5', text))
data = re.match('你好', text)
print(data.group())  # 匹配成功必须使用..group()才能输出内容

# 3.  re.search() 从起始位置开始匹配，返回第一个成功匹配到的对象
print(re.search('5', text).group())  # 匹配成功必须使用..group()才能输出内容

# 4.sub()  将匹配到的内容进行替换
print(re.sub('5', '啊', text))
print(re.sub('5', '啊', text, 1))  # 支持替换几个

# 5.  re.split()根据匹配到的动态内容，进行分割
print(re.split('\d+', text))
print(re.split('\d+', text, 1))  # 同样支持分割次数

# 6.  re.finditer()
print(re.finditer('\d+', text))  # 和findall()不同的是这个会先生成一个迭代器，不会一下子占用太多内存
for i in re.finditer('\d+', text):
    print(i.group())
print(next(re.finditer('\d+', text)).group())

# 7.正则的命名分组 (?P<名称>正则)
text = '你好adkj1568lqabcbad4545kwcwkjajkfas'
print(re.findall('(\d{2})(\d{2})', text))
print(re.findall('(?P<one>\d{2})(?P<two>\d{2})', text))
# 可以使用.finditer()获取
data = re.finditer('(?P<one>\d{2})(?P<two>\d{2})', text)
for item in data:
    print(item.groupdict())  # 提取字典格式
    print(item.group('one'))  # 也可以关键字获取想要的标签
