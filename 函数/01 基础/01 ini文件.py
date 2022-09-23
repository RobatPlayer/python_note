# Python提供了模块处理ini文件
import configparser  # 导入这个模块  configparser

config = configparser.ConfigParser()  # 固定搭配,后面有括号
config.read('file/my.ini', encoding='utf-8')  # 读取文件

# 1.获取所有的节点   .sections()
result = config.sections()  # 获取节点，比如[mysqld]
print(result)  # ['mysqld', 'mysqld_safe', 'client']

# 2.获取某个节点下所有的键值    .items('')
result = config.items('mysqld_safe')
# 得到的是列表里面套元组，分别是键和值   [('log-error', '/var/log/mariadb/mariadb.log'), ('pid-file', '/var/run/mariadb/mariadb.pid')]
print(result)
for key, value in result:
    print(key, value)

# 3.获取某个节点下键对应的值    .get(节点,键)
result = config.get('mysqld', 'log-bin')
print(result)

# 4.其他
# 4.1 判断是否存在这个节点，返回布尔值    .has_section('')
print(config.has_section('mysqld_safe'))

# 4.2添加节点     .add_section('节点')    .set(节点,键,值)
config.add_section('group')
config.set('group', 'name', 'zhangsan')  # 也可以添加键值
config.write(open('file/new_my.ini', 'w', encoding='utf-8'))  # 还要写入文件，文件可以是新的也可以是原来的

# 4.3删除节点或键值   .remove_section('节点')     .remove_option(节点,键)
config.remove_section('client')
config.remove_option('mysqld', 'log-bin')
config.write(open('file/new_my.ini', 'w', encoding='utf-8'))  # 删除之后必须写入文件才会变
