# 网络架构
# 交换机
'''
二层交换机只会维护接口和mac地址
三层交换机继承了交换机和路由器的功能
'''
'''
小型企业架构
运营商通过光猫将光纤的光信号转换成网络信号-->传入核心路由器（可以连接不同的运营商）-->防火墙-->核心交换机（三层）
-->接入交换机（二层）-->电脑

家庭架构
运营商通过光猫将光纤的光信号转换成网络信号-->家用路由器（集合了交换机和路由器的功能）-->家用设备
'''

# 互联网

# 网络核心词汇
'''
IP和子网掩码
    IP是一个32位的二进制，为了方便记忆将其分为4组，每组8位，由点.分割 ，将其转换成十进制就变成255.255.255.255最大
一个Ip地址可以划分为网络地址和主机地址：
    子网掩码255.255.255.0为了掩盖数据， 掩码覆盖掉的ip部分称为网络地址，剩下的部分叫主机地址 192.168.1.199/24意思就是前24位是
掩码，且都是1
    拆分IP的意义：网络地址相同的IP属于同一个网段。在局域网内只有同一个网段的IP才能相互通信，不同网段需要借助路由器才能通信
只要网络地址相同就属于同一个网段
'''

# DHCP服务：这个服务会将连接到路由器或交换机的设备自动设置IP地址，子网掩码，网关

'''
内网IP和公网IP
内网IP都用这些10.0.0.0到10.255.255.255，172.16.0.0到172.31.255.255，192.168.0.0到192.168.255.255
'''

'''
IPv4，长度32位，4个字节，格式A,B,C,D
IPv6，长度128位，16个字节，用冒号:分成八段XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX   每个x是一个16进制的数'''

'''
云服务器 :阿里云，腾讯云
'''

'''
端口：指定端口可以运行网站。例如网站A的端口8001，输入123.206.15.88:8001就可以访问A网站
端口的取值范围是0-65535，不过5000之前的好多都被计算机内部使用了
如果在浏览器只写IP不写端口会默认是80端口
'''

'''
域名：因为ip太难记，所有出现了域名。输入域名首先会寻找IP，然后在跳转IP'''