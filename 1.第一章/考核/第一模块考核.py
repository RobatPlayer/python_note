# 1. 分别解释"=","==","+="的含义(口述)
# =表示赋值，比如a=1,是将1的值赋给a
# ==表示比较，比较==两侧变量的值
# +=表示的是将后者的值加上再赋给前者，比如a+=1,表示a=a+1

# 2. 两个变量值的关系?(口述)
# x = 20
# y = 20
# x=y，x和y的值相等，都等于20

# 3. 请写出 “路飞学城” 分别用 utf-8 和 gbk 编码所占的位数(口述)
# "路飞学城"
# 在UTF-8编码中，一个中文占三个字节，一个字节等于8位，所以 "路飞学城"所占位数   4*3*8=96
# 在gbk编码中，一个中文字符占两个字节，   所以所占位数等于  4*2*8=64

# 4. 简述Python中的几种数据类型(口述)
# 整型，字符串，布尔类型，浮点型，列表，字典，元组，集合

# 5. 数据类型的可变与不可变分别有哪些?(口述)
# 可变：列表，字典，集合
# 不可变：整型，字符串，布尔类型，浮点型，元组

# 6. 元祖，列表，字典有没有长度的限制?(口述)
# 没有

# 7. 列表li = ['alex','egon','yuan','wusir','666'](编程)(3分钟)
li = ['alex', 'egon', 'yuan', 'wusir', '666']
# 7.1.把666替换成999
li[-1] = 999
print(li)

# 7.2.获取"yuan"04 索引和函数
print(li.index('yuan'))

# 7.3.假设不知道前面有几个元素，分片得到最后的三个元素( [-3:] )
print(li[-3:])

# 8. 将字符串s = “www.luffycity.com”给拆分成列表:li=['www','luffycity','com'] (编程)
s = "www.luffycity.com"
l = s.split('.')
print(l)

# 9. 对字典进行增删改查(编程)(5分钟)

d = {
    "Development": "开发小哥",
    "OP": "运维小哥",
    "Operate": "运营小仙女",
    "UI": "UI小仙女"
}
d.update({'name': '张三'})  # 增加
print(d)
del d['OP']  # 删除
print(d)
d['UI'] = '仙女'  # 修改
print(d)
print(d.get('UI'))  # 查找

# 10. 计算1+2+3...+98+99+100 (编程题)
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 11. 制作趣味模板程序(编程题)(5分钟) 需求:等待用户输入名字、地点、爱好，
# 根据用户的名字和爱好进行任意现实 如:敬爱可爱的xxx，最喜欢在xxx地方干xxx
message = input('请输入姓名、地点和爱好（以，隔开）：')
lst = message.split('，')
print(f'敬爱可爱的{lst[0]}，最喜欢在{lst[1]}地方干{lst[2]}')

# 12. 写一个三次认证(编程)(10分钟)

for i in range(1, 4):
    num = input('请输入账号:')
    pwd = input('请输入密码:')
    if num == '123456' and pwd == '1234':
        print('登录成功')
        break
    else:
        if i == 3:
            print('三次账号密码输入错误，请等待30s')
        else:
            print(f'账号或密码输入错误，还剩{3 - i}次机会')

# 13. 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,

for i in range(1, 4):
    num = input('请输入账号:')
    pwd = input('请输入密码:')
    if num == ('seven' or 'alex') and pwd == '123':
        print('登录成功')
        break
    else:
        if i == 3:
            print('三次账号密码输入错误，请等待30s')
        else:
            print(f'账号或密码输入错误，还剩{3 - i}次机会')

# 14.编写注册功能，注册成功则将用户的账号与密码保存到文件中，并且设置初始账户金额，一并存入文件中，若用户存在则不允许用户注册。
# 假设原有账号是这些

lst = [{'账号': '123456', '密码': '1111', '余额': 100}, {'账号': '10086', '密码': '2222', '余额': 300}]
dic = {}
while True:
    num = input('请输入您创建的账号：')
    flag = True
    for i in lst:
        if i.get('账号') == num:  # 判断账号是否已经存在
            print('账号已存在，请重新输入要创建的账号')
            flag = False
            break
        continue
    if flag:
        print('可以创建此账号')
        pwd = input('请输入您创建账号的密码')  # 创建密码
        money = 0  # 创建余额
        break
dic.update({'账号': num, '密码': pwd, '余额': money})
lst.append(dic)  # 将新创建的账号添加到总库中
print(lst)
with open('message.text', mode='w', encoding='utf-8') as file:  # 写入文件
    for i in lst:  # {'账号': '123456', '密码': '1111', '余额': 100}
        file.write(str(i))
        file.write('\n')

# 15.用户密码修改功能

# 假设原有账号是这些
lst = [{'账号': '123456', '密码': '1111', '余额': 100}, {'账号': '10086', '密码': '2222', '余额': 300}]
while True:
    num = input('请输入账号:')
    pwd = input('请输入密码:')
    flag = True
    for i in lst:
        if i.get('账号') == num and i.get('密码') == pwd:  # 账号存在
            print('登陆成功，请修改密码')
            new_pwd = input('请输入新的密码：')
            i.update({'密码': new_pwd})  # 更新原账号
            flag = False
            break
    if flag:  # 输入错误
        print('账号或密码输入错误')
        continue
    break
print(lst)
with open('new_message.text', mode='w', encoding='utf-8') as file:  # 写入文件
    for i in lst:  # {'账号': '123456', '密码': '1111', '余额': 100}
        file.write(str(i))
        file.write('\n')

# 16.用户充值功能(ps: 文件的金额进行修改，重新保存即可)
# 假设原有账号是这些
lst = [{'账号': '123456', '密码': '1111', '余额': 100}, {'账号': '10086', '密码': '2222', '余额': 300}]
while True:
    num = input('请输入账号:')
    pwd = input('请输入密码:')
    flag = True
    for i in lst:
        if i.get('账号') == num and i.get('密码') == pwd:  # 账号存在
            print('登陆成功')
            while True:
                try:
                    money = int(input('请输入充值金额：'))
                    new_money = i.get('余额') + money
                    i.update({'余额': new_money})  # 更新余额信息
                    print(f'充值成功，您当前余额为{i.get("余额")}')  # 展示余额信息
                    break
                except:
                    print('输入格式错误,请重新输入')
                    continue
            flag = False
            break
    if flag:  # 输入错误
        print('账号或密码输入错误,请重新输入')
        continue
    break
print(lst)
with open('money_message.text', mode='w', encoding='utf-8') as file:  # 写入文件
    for i in lst:  # {'账号': '123456', '密码': '1111', '余额': 100}
        file.write(str(i))
        file.write('\n')
