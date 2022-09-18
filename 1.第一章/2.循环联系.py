# 1.猜数字
# num = 66
# while True:
#     try:
#         guess = int(input('请输入您猜的数字：'))
#         if guess == 66:
#             print('猜对了')
#             break
#         elif guess < 66:
#             print('猜小了')
#         elif guess > 66:
#             print('猜大了')
#     except:
#         print('输入错误')
# print('over!')

# 2.输出1-100整数
i = 1
a = []
while i <= 100:
    a.append(i)
    i += 1
print(a)

for i in range(1, 11):
    if i != 7:
        print(i, end=' ')
print()

sum=0
for i in range(1,101):
    if i%2==0:
        i=-i
    sum=sum+i
print(sum)