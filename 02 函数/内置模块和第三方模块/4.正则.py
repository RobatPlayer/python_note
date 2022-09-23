import re

# 1.字符相关
text = '你好adkj156lqabcbad4545kwcwkjajkfas'
print(re.findall('a', text))  # 寻找所有的a字符   re.findall('a', 变量)

print(re.findall('[abc]', text))  # 提取所有的a或b或c

print(re.findall('q[abc]', text))  # 提取所有的qa或qb或qc

print(re.findall('[^abc]', text))  # 提取除abc以外的所有字符

print(re.findall('[1-9]', text))  # 提取1-9

# .代指除了换行符以外的所有字符
# .+表示贪婪匹配 如
print(re.findall('a.+k', text))

# .+?表示非贪婪匹配
print(re.findall('a.+?k', text))

# \w表示字母数字下划线和汉字

# \d代表整数

# \s代表空白字符，换行

# 2.数量相关
# *表示重复0次或更多次

# +表示重复1次或更多次

# ?表示重复0次或一次

# {n} 重复n次

# {n,} 重复n次或更多次

# {n,n} 重复n到m次，都带等号

# 3.括号
# 如果提取中含有括号，则只会提取到括号里面的内容，括号不影响判定
text = '你好adkj156lqabcbad4545kwcwkjajkfas'
print(re.findall('j(.+?)k', text))

# 也可以加多个括号
print(re.findall('j(\d+)(lq)', text))

# 提取指定区域或条件
text = '131aefaef你好啊哈哈13156562'
print(re.findall('131(\w+f|\d{5})', text))  # |表示或的意思
print(re.findall('aefaef(.*?)1', text))
print(re.findall('\d', text))  # 如果只输入\d 会遍历

print(re.findall('\w+', text, re.ASCII))  # 如果在后面加上re.ASCII就不会匹配到中文

# 起始和结束
# 提取的内容必须是指定的开头和结尾
# 开始^    结束$

# 特殊字符，如果文本中还有.-{（类似，需要用\转义

print(re.findall('131(.*?)你',text))