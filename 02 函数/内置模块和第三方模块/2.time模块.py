# 时间处理
# UTC/GMT 这个是世界时间
# 本地时间：本地时区的时间

# ##time模块
import time

# 1.获取当前的时间戳，是本地时间time.time()
print(time.time())  # 1647699299.708626 从1970年开始到现在过了多少秒

# 2.获取时区  time.timezone
v1 = time.timezone  # -28800  获取当前时间区
print(v1)
print(v1 / 60 / 60)  # -8.0 表示东八区

# 3.睡眠时间，单位秒   time.sleep(x)
print('开始')
# time.sleep(3)
print('结束')

# 百分比下载
print('下载开始')
for i in range(1, 101):
    print(f'\r{i}%', end='')  # 输入\r会将光标放在最前面，加end=''保证不会换行输出。下次输入覆盖内容
    time.sleep(0.02)
print('\n下载完成')
