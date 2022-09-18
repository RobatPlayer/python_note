# 1.请用代码实现如下进制的转换
v1 = 675  # 请将v1转换为二进制（字符串类型）。
print(bin(v1))
v2 = "0b11000101"  # 请将二进制v2转换为十进制（整型）
print(int(v2, base=2))
v3 = "11000101"  # 请将二进制v3转换为十进制（整型）
print(int(v3, base=2))
print('------------------------------------')
# 2.按要求实现
'''现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，
然后将两个二进制拼接起来，最终再转换为整型（十进制）。'''
v1 = 123
v2 = 456
v3 = bin(v1).lstrip('0b') + bin(v2).lstrip('0b')
# print(bin(v1))
# print(bin(v2))
# print('-------------------')
# print(bin(v1).lstrip('0b1'))
# print(bin(v2).lstrip('0b'))
# print(bin(v1)[2:])
# print(bin(v2)[2:])
print(v3)
print(int(v3, base=2))
print('-----------------------------------------')

# 3.
'''现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，
再补足为2个字节（16位），然后将两个二进制拼接起来，最终再转换为整型（十进制）。
例如：
​	123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011" ，补足16位为  "00000000 01111011"
​	456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"，，补足16位为  "00000001 11001000"
​	将两个二进制拼接起来的值为："00000000 0111101100000001 11001000"，再将此值转换为整型为：8061384
'''  # 00000000 01111011 00000001 11001000
v1 = 123
v2 = 456
v3 = (bin(v1).lstrip('0b')).zfill(16) + (bin(v2).lstrip('0b')).zfill(16)
# print((bin(v1).lstrip('0b')).zfill(16))
# print((bin(v2).lstrip('0b')).zfill(16))
# print(v3)
print(int(v3, base=2))
print('------------------------------------------')
# 4.列举你了解的那些数据类型的值转换为布尔值为False。
l = [0, '', {}, [], (), set()]
for i in l:
    print(bool(i))
print('--------------------------------')

# 5.看代码写结果：
'''
if "":
    print(123)
else:
    print(456)    456

if 0:
    print(999)
else:
    print(666)   666

if "武沛齐":
    print(345)  345
else:
    print(110)
'''
# 6.让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。
# text=input('请输入文本')
# text=text.replace('苍老师','***').replace('波波老师','***')
#
# print(text)

# 7.有变量name = "aleX leNb " 完成如下操作：
name = "aleX leNb "
print(name.strip())
print(name.startswith('al'))
print('Nb' == name[-1:-2])
print(name.endswith('Nb'))
print(name.replace('l', 'p'))
print(name.split('l'))
print(name.upper())
print(name.lower())
print('--------------------------------')
'''
- 移除 name 变量对应的值两边的空格,并输出处理结果
- 判断 name 变量是否以 "al" 开头,并输出结果（用切片 或 startswith实现）
- 判断name变量是否以"Nb"结尾,并输出结果（用切片 或 endswith实现）
- 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果 
- 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
- 将name变量对应的值根据第一个"l"分割,并输出结果
- 将 name 变量对应的值变大写,并输出结果
- 将 name 变量对应的值变小写,并输出结果
'''

# 8.如何实现字符串的翻转？
print(name[::-1])
print('--------------------------------')
# 9.有字符串s = "123a4b5c"
s = "123a4b5c"
print(s[:3])
print(s[3:6])
print(s[-1])
print(s[-3::-2])
print('--------------------------------')
'''
- 通过对s切片形成新的字符串 "123"
- 通过对s切片形成新的字符串 "a4b"
- 通过对s切片形成字符串 "c"
- 通过对s切片形成字符串 "ba2"
'''

# 10.使用while循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
message = "伤情最是晚凉天，憔悴厮人不堪言"
i = 0
while True:
    if i <= len(message) - 1:
        print(message[i], end=' ')
        i += 1
    else:
        break
print()
# 11.使用for循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
for i in message:
    print(i, end=' ')
print()
print('--------------------------------')

# 12.使用for循环和range实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行倒叙输出。
for i in range(len(message) - 1, -1, -1):
    print(message[i], end=' ')
print()
print('--------------------------------')

# 13.使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
i = 3
for _ in range(3):
    print(f'倒计时{i}秒')
    i -= 1
print('--------------------------------')

# 14.让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。
# text = input('请输入一段文本')
# l = text.split('浪')
# print(l)
# print(len(l)-1)
text = input('请输入一段文本：')
a = 0
for i in text:
    if i == '浪':
        a += 1
print(a)
# 15.获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）：
'''
a = input('第一次内容：')  # wafawf12312wafadaw12
b = input('第二次内容：')
l = []
sum = 0
for i in a:
    if i.isdecimal():
        l.append(i)
for i in b:
    if i.isdecimal():
        l.append(i)
print(l)
for i in l:
    num = int(i)
    sum += num
print(sum)
'''
