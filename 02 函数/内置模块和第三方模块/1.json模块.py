# 1.json
import json

# json格式是一种数据格式，本质上是字符串
value = '[{"id": 45, "age": 12}, ["hello",123]]'  # json里面都是双引号，而且没有括号，只有[]和{}
# json格式用于不同系统交互，比如Python和Java
data = [{"id": 45, "age": 12}, ["张三", 123], ('李四', 'asf')]
res = json.dumps(data)  # 将Python格式转换成json格式,称为序列化  json.dumps(x)

print(res)  # [{"id": 45, "age": 12}, ["\u5f20\u4e09", 123], ["\u674e\u56db", "asf"]]  没有括号,中文变成了Unicode编码

print(json.dumps(data, ensure_ascii=False))  # 在变量后面加入ensure_ascii=False中文就不会转变

# 同样json格式也能转换成Python格式 ,称为反序列化  json.loads(x)
print(json.loads(res))
