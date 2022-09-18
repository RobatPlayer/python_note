# 二进制和八进制以及十六进制只能通过十进制进一步转换，不能直接转换,类型都是字符串
print(bin(12))
a = bin(12)
# print(hex(a))   TypeError: 'str' object cannot be interpreted as an integer
print(int('0b0101110101', base=2))  # 可以这样装换成十进制

# 单位
# 1B=8b  1字节等于8位
# 1KB=1024B
# 1M=1024kb
print(chr(65))
print(ord('a'))

# 将字符串转换成字节，一般用于存储
print('张'.encode('gbk'))
print('张'.encode('utf-8'))
c = '张'.encode('utf-8')
print(c.decode('utf-8'))

name = '张三'
print(len(name))
