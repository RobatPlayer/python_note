# 1.判断布尔值
a = 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# f or t or f and t and t or f
# f or t or f or f
# true
b = not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# not t and t or f and t and t or f
# f and t or f or f
# false

# 2.
c = 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8 or 4 or 0 or 7
# 8
d = 0 or 2 and 3 and 4 or 6 and 0 or 3
# 0 or 4 or 0 or 3
# 4 or 0 or 3
# 4

# 3.
a = 6 or 2 > 1
# 6 or t
# 6

a = 3 or 2 > 1  # 3
a = 0 or 5 < 4  # false
a = 5 < 4 or 3  # 3
a = 2 > 1 or 6  # true
a = 3 and 2 > 1  # true
a = 0 and 3 > 1  # 0
a = 2 > 1 and 3  # 3
a = 3 > 1 and 0  # 0
a = 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# t and 2 or f and 3 and 4 or t
# 2 or f or t
# 2

# 4.实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）。
'''
i = 3
while True:
    name = input('请输入用户名：')
    try:
        pwd = int(input('请输入密码:'))
        if name == 'user' and pwd == 123456:
            print('登陆成功')
            break
        else:
            i -= 1
            if i != 0:
                print(f'用户名或密码输入错误，还剩{i}次机会')
                continue
            else:
                print('用户名或密码连续输入三次错误，请稍后再试')
                break
    except:
        print('输入格式错误，请重新输入')
print('系统已退出')
'''
# 5. 猜年龄游戏.要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。
'''
age = 23
i = 3
while True:
    i -= 1
    try:
        guess = int(input('请输入您猜的年龄：'))
        if guess == age:
            print('恭喜你，猜对了')
            break
        elif guess > age and i != 0:
            print(f'猜大了，还剩{i}次机会')
            continue
        elif guess < age and i != 0:
            print(f'猜小了，还剩{i}次机会')
            continue
        else:
            print('猜错三次了，自动退出系统')
            break
    except:
        print('输入格式错误，只能输入整数')
print('退出系统')
'''
# 6. 猜年龄游戏升级版.要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，
# 就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
age = 23
i = 3
while True:
    i -= 1
    try:
        guess = int(input('请输入您猜的年龄：'))
        if guess == age:
            print('恭喜你，猜对了')
            break
        elif guess > age and i != 0:
            print(f'猜大了，还剩{i}次机会')
            continue
        elif guess < age and i != 0:
            print(f'猜小了，还剩{i}次机会')
            continue
        else:
            try:
                question = input('猜错三次了，是否重新玩?Y/N')
                if question == 'Y' or 'y':
                    i = 3
                    continue
                else:
                    print('系统退出')
                    break
            except:
                print(f'输入格式错误')

    except:
        print('输入格式错误，只能输入整数')
print('退出系统')
