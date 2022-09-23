# 当去执行一个py文件时__name__='__main__'
print(__name__)
# 如果导入一个py文件时，他里面的__name__='文件名'
if __name__ == '__main__':
    pass

# 主文件越简单越好，会调运大量的其他函数，一般都有if __name__ == '__main__':

