# 函数定义的位置：函数不仅可以定义在全局作用域，而且可以定义在局部作用域
# 嵌套函数可以避免和他人代码名字重复
# 每个函数在执行时，会重新创建一个新的作用域
# 1.优先在自己作用域找，没有再去上一层
# 2.在作用域寻找时，要确保此次值是什么
# 3.分析函数的执行，并确定函数作用域链

# ##闭包  并行下载，多线程下载
from concurrent.futures.thread import ThreadPoolExecutor
import requests


def task(url):
    res = requests.get(url=url)
    return res.content


# 下载完成之后，Python内部会自动执行的函数
def outer(file_name):
    def done(arg):
        # 参数就是下载的视频内容
        content = arg.result()
        with open(file_name, mode='wb') as file:
            file.write(content)

    return done


# 线程池，10个人
POOL = ThreadPoolExecutor(10)
video_dict = {
    "1": {"title": "东北F4模仿秀",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
    "2": {"title": "卡特扣篮",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
    "3": {"title": "罗斯mvp",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
}

for i in video_dict.values():
    print(i.get('url'))
    # 去线程池找个人下载这个视频
    future = POOL.submit(task, url=i.get('url'))  # 执行这个函数（函数内部定义下载逻辑）   future是一个临时值，不是函数返回值
    # d当执行完成下载完成函数，后会自动执行某个函数
    future.add_done_callback(outer(i.get('title')))
    print(i)
