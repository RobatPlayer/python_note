# 自己去网上搜索如何基于Python计算mp4视频的时长，最终实现用代码统计某个文件夹下所有mp4的时长。
import os
import time
from moviepy.editor import VideoFileClip


def video_time(path):
    ''' 这个是计算视频时长的函数'''
    cilp = VideoFileClip(path)
    return cilp.duration


def file_path(data):
    '''这是一个获取文件路径的函数'''
    l = []
    for path, folder, file_lst in data:
        for file in file_lst:
            file_abs = os.path.join(path, file)
            if file_abs.rsplit('.')[-1] == 'mp4':
                l.append(file_abs)
    return l


def calc_time(st):
    '''这是将字符串转换成时间的函数'''
    return time.strftime('%H:%M:%S', time.gmtime(st))


path = os.walk(r'G:\usr')
sum = 0
for i in file_path(path):
    sum += video_time(i)
print(sum)
print(calc_time(sum))

# a = '2019-5-10 00:00:36'
# print(time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S')))
# print(datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
