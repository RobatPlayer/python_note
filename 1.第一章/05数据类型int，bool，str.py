# ##整型
a = 10
a.bit_length()  # .后面的是独有功能,获取10的二进制有多少位组成
print(bin(10))
print(a.bit_length())
# 转换


# ##布尔类型
# 转换，任何类型都可以转换成布尔类型  0和各种空转换成False

# ##字符串类型（18/48）
# 独有功能
'asf'.encode()  # .功能()

# 1.判断字符串是否以XX开头  .startswith(x)
a = '你好世界'
print(a.startswith('你好'))  # 得到的是一个布尔值

# 2.以XX结尾   .endswith(x)
print('helloworld'.endswith('ol'))

# 3.判断字符串是否为十进制的数    .isdecimal()
print('123465'.isdecimal())  # 得到的是布尔值

# 4.为字符串去除两边空白，换行，制表符，得到一个新的字符串    .strip(x)
print('    he  l l o , wo r ld      '.strip())  # 两边的空白，中间不行
print('    he  l l o , wo r ld      '.lstrip())
print('    he  l l o , wo r ld      '.rstrip())
print('    he  l l o , wo r ld      '.replace(' ', ''))
print('\nhello\tworld\t'.strip())
print('helloworld'.strip('d'))  # 也可以去除指定字符

# 5.将字符串的内容变成大写   .upper()
print('helloworld'.upper())

# 6.字符串变小写   .lower()
print('HelloWORLD'.lower())

# 7.字符串内容替换    .replace(a,b)
print('你是好人，好人一生平安'.replace('平安', '幸福'))  # 出现新的字符串
# content=input('输入信息')
# content.replace('草','*')

# 8.字符串切割   .split(x,1)
print('hello|world|hello'.split('|'))  # 得到的是一个列表
print('xx/xx/xxx/xx/xx.mp4'.rsplit('/', 1))

# 9.字符串拼接  .join(x)
print('-'.join('world'))  # 将后者用前者拼接，可以是列表,得到是字符串,和split相反
print('-'.join(['hello', 'world', 'hello']))

# 10.格式化字符串，占位符

# 11.字符串转换为字节   .encode(x)常用于文件存储
print('张三'.encode('utf-8'))
print('张三'.encode('gbk'))
print(b'\xd5\xc5\xc8\xfd\xde\xfe'.decode('gbk'))

# 12.将字符串内容居中/左/右   .center(20,x)   .rjust(20,x)
print('张三'.center(20, '*'))
print('张三'.rjust(20))

# 13.帮助填充0   .zfill(20)  面试常用，处理二进制数据
print('张三'.zfill(20))
# 应用场景
print('101'.zfill(8))  # 凑够八个字节

# ##公共功能
# 1.相加
# 2.相乘
# 3.长度
# 4.获取字符串的字符，通过索引 。只能读取数据，不能修改
for i in 'helloworld':
    print(i, end=' ')
print()

# 5.切片  [x:x:x]   只能读取数据，不能修改
print('helloworld'[1:6:2])

# 6.步长  面试题：反转字符串
print('helloworld'[-1::-1])

# 7.for循环
# while一般用于无限制（未知）循环  ，for in循环用于已知循环次数。都可以使用break和continue


# ##转换
# 一般整型才转换


# ##字符串不能被修改

