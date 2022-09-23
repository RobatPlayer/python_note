# csv也称字符分割值，一般用逗号，也可以不是
# 下载所有图片，以名字命名
import requests
import os

with open('file/美女.csv', mode='r', encoding='utf-8') as file:
    # 去掉表头
    file.readline()
    for line in file:
        # print(line)
        id, name, url = line.strip().split(',')
        # print(url)
        # 下载图片
        requ = requests.get(url)

        # 判断下载的目录是否存在
        if not os.path.exists('file/图片'):
            os.makedirs('file/图片')  # 不存在就创建目录
        with open(f'file/图片/{name}.png', mode='wb') as dowload_file:  # 必须确保文件夹存在，
            dowload_file.write(requ.content)
print('over!')
