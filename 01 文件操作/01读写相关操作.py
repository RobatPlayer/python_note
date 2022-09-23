# ##读
with open('file/info.txt', mode='r', encoding='utf-8') as file:
    # 默认读所有
    print(file.read())

    # 读n个字符   .read(n)   ，如果是rb将是读字节,可以分段读   网络传输常用
    file.seek(0)
    print(file.read(1))

    # 读一行   常用
    file.seek(0)
    print(file.readline())

    # 读所有行，最后生成列表,每行作为一个元素
    file.seek(0)
    print(file.readlines())

    # 循环，读大文件 200G   不知道有多少行   常用
    file.seek(0)
    for i in file:
        print(i.strip())

# ##写
with open('file/infofo.txt', mode='w+', encoding='utf-8') as file:
    # 立即写入硬盘   file.flush()
    file.flush()

    # 移动光标，到指定字节位置  字节，无论什么模式  .seek(x)    在a模式下调整光标没有用
    file.seek(3)  # 如果移动到汉字里面。会产生乱码

    # 获取当前光标位置    .tell()   获取的永远是字节的位置
    print(file.tell())

# ##with可以同时打开多个文件
with open('logo.txt',mode='r') as f1,open('logo2.txt','w') as f2:
    pass