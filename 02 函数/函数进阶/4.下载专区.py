import requests
import os

# 可供下载的图片
IMAGE_DICT = {
    "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
    "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
    "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
    "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
}

# 可供下载的短视频
VIDEO_DICT = {
    "1": {"title": "东北F4模仿秀",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
    "2": {"title": "卡特扣篮",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
    "3": {"title": "罗斯mvp",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
}

# 可供下载的集锦
NBA_DICT = {
    "1": {"title": "威少奇才首秀三双",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
    "2": {"title": "塔图姆三分准绝杀",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}
}


def img_dowload():
    ''' 这个下载图片的函数 '''
    while True:
        print('有以下内容可供下载')
        lst = []
        for i, value in enumerate(IMAGE_DICT.values(), 1):
            print(i, value[0])
            i = str(i)
            lst.append(i)
        number = input('请输入想下载图片的序号(q或Q退出):')
        if number.lower() == 'q':
            return
        if number not in lst:
            print('输入错误，请重新输出')
            continue
        url = IMAGE_DICT.get(number)[1]  # 根据键获取值，再根据索引获取url
        img_name = IMAGE_DICT.get(number)[0]  # 获取下载图片文件的名字
        IMAGE_DICT.pop(number)  # 根据键移除下载的图片
        lst.remove(number)  # 移除判断元素
        res = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        )
        if not os.path.exists('img'):
            os.makedirs('img')
        with open(f'img/{img_name}.png', mode='wb') as file:  # 创建文件下载路径
            file.write(res.content)  # 写入下载文件的内容
            print('下载完成')


def short_video():
    ''' 这个下载短视频的函数 '''
    while True:
        print('有以下内容可供下载')
        lst = []
        for i, value in enumerate(VIDEO_DICT.values(), 1):
            print(i, value.get('title'))
            i = str(i)
            lst.append(i)
        number = input('请输入想下载视频的序号(q或Q退出):')
        if number.lower() == 'q':
            return
        if number not in lst:
            print('输入错误，请重新输出')
            continue
        url = VIDEO_DICT.get(number).get('url')  # 根据键获取值，再根据键获取url
        video_name = VIDEO_DICT.get(number).get('title')  # 获取下载图片文件的名字
        VIDEO_DICT.pop(number)  # 根据键移除下载的视频
        lst.remove(number)  # 移除判断元素
        res = requests.get(
            url=url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
            }
        )
        if not os.path.exists('video'):
            os.makedirs('video')
        with open(f'video/{video_name}.mp4', mode='wb') as file:  # 创建文件下载路径
            file.write(res.content)  # 写入下载文件的内容
        print('下载完成')


def nba_fragment():
    ''' 这个下载NBA集锦的函数 '''
    while True:
        print('有以下内容可供下载')
        lst = []
        for i, value in enumerate(NBA_DICT.values(), 1):
            print(i, value.get('title'))
            i = str(i)
            lst.append(i)
        number = input('请输入想下载集锦的序号(q或Q退出):')
        if number.lower() == 'q':
            return
        if number not in lst:
            print('输入错误，请重新输出')
            continue
        url = NBA_DICT.get(number).get('url')  # 根据键获取值，再根据键获取url
        nba_name = NBA_DICT.get(number).get('title')  # 获取下载图片文件的名字
        NBA_DICT.pop(number)  # 根据键移除下载的视频
        lst.remove(number)  # 移除判断元素
        res = requests.get(
            url=url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
            }
        )
        if not os.path.exists('nba'):
            os.makedirs('nba')
        with open(f'nba/{nba_name}.mp4', mode='wb') as file:  # 创建文件下载路径
            file.write(res.content)  # 写入下载文件的内容
        print('下载完成')


while True:
    print('----------------------欢迎来到资源下载器----------------------')
    print('1.下载 花瓣网图片专区')
    print('2.下载 抖音短视频专区')
    print('3.下载 NBA锦集 专区')
    num = input('请输入序号进入以上专区(q/Q退出系统):')
    if num.lower() == 'q':
        break
    if num not in ['1', '2', '3']:
        print('输入错误,请重新输入：')
        continue
    elif num == '1':  # 是否可以通过函数作为变量来减少if的次数  ！可以
        img_dowload()
    elif num == '2':
        short_video()
    elif num == '3':
        nba_fragment()
