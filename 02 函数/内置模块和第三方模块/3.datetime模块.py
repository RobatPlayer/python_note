from datetime import datetime, timezone, timedelta
import time

# 1.获取当前本地时间   datetime.now()
print(datetime.now(), type(datetime.now()))  # 2022-03-19 22:35:12.861438 这个格式  而且是一种特殊的数据类型，是一个类

# 2.获取utc时间  datetime.utcnow()
print(datetime.utcnow())

# 3.获取指定时区的时间 需要timezone和timedelte模块
# 首先定义一个时区  timezone(timedelta(hours=7))
tz = timezone(timedelta(hours=7))  # 这个表示东7区
print(datetime.now(tz=tz))  # 这样就可以获取到东7区的时间

# 4.时间加减   +- timedelta(days=,hours=,minutes=)
v1 = datetime.now()
print(v1)
v2 = v1 + timedelta(days=10, hours=5, minutes=30)
print(v2)
print(v1 - timedelta(hours=10))

# 5.获取时间间隔  都是datetime类型不能相加
v1 = datetime.now() - datetime.utcnow()
print(datetime.now() - datetime.utcnow())  # 8:00:00
print(datetime.utcnow() - datetime.now())  # -1 day, 16:00:00
print(v1.days, v1.seconds, v1.microseconds)  # 可以获得以天，秒，毫秒为单位的数值

print(datetime.now() > datetime.utcnow())  # True也可以比较

# 6.字符串和datetime类型转化，两种代码只差了一个字母
# 字符串转datetime   datetime.strptime(变量，格式)
text = '2022-3-02'  # 字符串必须通过-分割，不能有空格
print(datetime.strptime(text, '%Y-%m-%d'))  # 这个-不能变
print(datetime.strptime(text, '%Y-%m-%d') - datetime.now())  # 转化之后就可以和上面相加减

# datetime转字符串   变量.strftime(格式)
v1 = datetime.now()
print(v1.strftime('%Y-%m-%d %H-%M-%S'))
print(v1.strftime('%Y:%m:%d %H:%M:%S'))  # 这个格式可以变成：连接

# 7.时间戳
# 时间戳格式转行datetime格式    datetime.fromtimestamp(时间戳)
ctime = time.time()
print(datetime.fromtimestamp(ctime))

# datetime格式转换成时间戳    变量.timestamp()
v1 = datetime.now()
print(v1.timestamp())

# 可以看出其他转换成datetime变量都在后面括号里，反过来变量在前面.
# 字符串和时间戳一般都会转化成datetime进行加减比较

