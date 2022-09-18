# 集合  无序，   可变，  不允许重复  不能通过索引获取
s = set()  # 空集合

#  ##独有功能
# 1.添加元素   .add(x)
s.add('周杰伦')
print(s)

# 2.删除元素   .remove()    .discard()
s.remove('周杰伦')
print(s)
s = {'张三', '李四', 13456, 789}
s.discard(13456)
print(s)

# 3.交集   .intersection(x)   &  会得到新的集合
s1 = {'张三', '李四', 13456, 789}
s2 = {'张三', '李四', 'hello'}
print(s1 & s2)
print(s1.intersection(s2))

# 4.并集    .union(x)   |
print(s1.union(s2))
print(s1 | s2)

# 5.差集   .difference(x)  前者有后者没有的值  s1-s2
print(s1.difference(s2))
print(s1 - s2)

#  ##公共功能
# 1.计算差集
# 2.交集
# 3.并集
# 4.长度
# 5.for 循环


#  ##类型转化  set() 可以转字符串，列表，元组  可以去除相同元素
# 集合里面不能有列表和集合
# 在集合里面1和True以及0和False不能同时存在


# ##None类型：节省内存
d = {None: 123}
print(d)

print(['0012','00210'])