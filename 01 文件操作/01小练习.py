# 筛选出股票 当前价大于 20 的所有股票数据。
with open('file/股票.txt', encoding='utf-8') as file:
    # 首先跳过第一行
    file.readline()  # 读完光标会移动
    # 接着往下读
    for i in file:
        price = float(i.split(',')[2])
        # if price > 20:
        #    print(i.strip())
        if price <= 20:
            continue
        print(i.strip())

# 修改文件
# 读取所有文件信息，通过replace替换   (适用于小文件,不适用大文件)
# 挨个位置找，在替换 ，这是不可行的，因为字符串的长度不同，直接替换会出错  （不可取）
# 同时打开两个文件，一个读一个写  （适用于大小文件）   推荐这么用
with open('file/ha.conf', 'r') as read_file, open('file/new_ha.conf', 'w') as write_file:
    for line in read_file:
        new_line = line.replace('luffycity', 'pythonav')
        write_file.write(new_line)

# ##重命名文件    shutil.move(a,b)
import shutil

shutil.move('file/new_ha.conf', 'file/ha.conf')  # 如果原名字存在，则会覆盖
