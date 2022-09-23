from xml.etree import ElementTree as ET

# 4.1
ml = '''<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
'''
# 打开文件   ET.parse()
tree = ET.parse('file/xm.xml')

# 获取根标签     tree.getroot()
root = tree.getroot()
print(root)

# 如果获取到的是字符串,可以直接这样获取根标签   ET.XML(x)
print(ET.XML(ml))

# 4.2
# 获取子标签,遍历   获取第一个值是子标签的值，第二个是子标签的属性，字典形式  {'name': 'Liechtenstein'}
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.attrib, i.text)  # 获取标签，属性，以及文本内容

# 也可以使用find   .find()  只找第一个    .findall()找所有标签
print(root.find('country').findall('neighbor'))
v2 = root.find('country').find('year')
print(v2.text)

# 4.3
# 修改标签
v2 = root.find('country').find('year')
v2.text = '9999'  # 修改文本  ,必须是字符串
v2.set('update', '2022.3.17')  # 增加节点

# 保存文件
tree = ET.ElementTree(root)
tree.write('file/new_ml.xml', encoding='utf-8')

# 删除标签   .remove()
v3 = root.find('country')  # 只能删除根标签！
root.remove(v3)

# 4.4构建xml文件
# 创建根标签   ET.Element()
root = ET.Element('home')
son1 = ET.Element('son', {'name': '儿'})
grandson1 = ET.Element('grandson', {'name': '孙'})

# 添加标签   .append
son1.append(grandson1)
root.append(son1)

# 保存文件
tree = ET.ElementTree(root)
tree.write('file/my.xml', encoding='utf-8', short_empty_elements=True)  # short_empty_elements=是否生成短标签
# <grandson name="孙" />  标签里面没有值，可以这么写，称作短标签

# 第二种方法
root = ET.Element('famliy')
son1 = root.makeelement('son1', {'name': 'son'})  # .makeelement()  创建完成之后和根标签没有关系，后续还要添加

# 第三种（最简单）  ET.SubElement(根标签，子标签名字，属性)
root = ET.Element('famliy')
son3 = ET.SubElement(root, 'son', {'name': 'son'})  # ET.SubElement(根标签，子标签名字，属性)
sun3 = ET.SubElement(son3, 'sun', {'age': '12'})
sun3.text = '孙子'
tree = ET.ElementTree(root)
tree.write('file/simple.xml', encoding='utf-8')

# 练习 ，获取标签键值，字典类型
content = """<xml>
    <ToUserName><![CDATA[gh_7f083739789a]]></ToUserName>
    <FromUserName><![CDATA[oia2TjuEGTNoeX76QEjQNrcURxG8]]></FromUserName>
    <CreateTime>1395658920</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[TEMPLATESENDJOBFINISH]]></Event>
    <MsgID>200163836</MsgID>
    <Status><![CDATA[success]]></Status>
</xml>"""
root = ET.XML(content)
dic = {}
for i in root:
    print(i.tag, i.text)  # 可以直接将CDATA里面的内容提取出来
    dic.update({i.tag: i.text})
print(dic)
