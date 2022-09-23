def info():
    print('第一行')
    print('第二行')


info()
# 有重复代码
# 代码太长

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

'''
# 1.邮箱配置服务
msg = MIMEText('hello，what are you doing??', 'html', 'utf-8')  # 邮箱的内容
msg['From'] = formataddr(['帅哥', 'halloworld2022@126.com'])  # 发件人信息
msg['Subject'] = '约吗？'

# 2. 发送邮件
server = smtplib.SMTP_SSL("smtp.126.com")
server.login("halloworld2022@126.com", "LWZSPNNEBGRAZFTW")
server.sendmail("halloworld2022@126.com", "291785283@qq.com", msg.as_string())
server.quit()
'''


# 引入函数的参数,这个参数是可变的，可以很方便利用
def send_email(email):
    msg = MIMEText('hello，what are you doing??', 'html', 'utf-8')  # 邮箱的内容
    msg['From'] = formataddr(['帅哥', 'halloworld2022@126.com'])  # 发件人信息
    msg['Subject'] = '约吗？'
    server = smtplib.SMTP_SSL("smtp.126.com")
    server.login("halloworld2022@126.com", "LWZSPNNEBGRAZFTW")
    server.sendmail("halloworld2022@126.com", email, msg.as_string())
    server.quit()


# send_email('2574989742@qq.com')

# 1.形参
# 2.实参
# 3.位置传参
# 4.关键字传参   mode='w'  如果位置传参和关键字传参混合用，位置传参在前，关键字传参在后
def fun(a1, a2, a3):
    pass


fun(1, a3=2, a2=6)


# 动态参数
# *个数可变的位置参数，只能通过位置传参
def fun1(*args):  # 得到结果是一个元组
    pass


# **个数可变的关键字参数,只能通过关键字传参
def fun2(**kwargs):  # 得到结果是一个字典
    pass


# *  **两个合用
def fun3(*args, **kwargs):
    pass


fun3(22, 33, 99, n1='张三', n2=18)


# 函数的返回值
# 1.返回值可以是任意类型，如果什么都不写，会返回None
# 2.如果return后面有逗号，结果会变成元组
# 3.函数如果再运行中遇到return会立刻终止后面所有代码
def fun5():
    print(1)
    return '结束了'
    print(2)


ret = fun5()
print(ret)
