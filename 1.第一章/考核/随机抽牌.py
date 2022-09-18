# 补充代码实现《棋牌游戏11点》需求：生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示)3个玩家
# 发牌规则默认先给用户发一张牌，其中J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
# 用户根据自己的情况判断是否继续要牌。要，则再给他发一张。不要，则开始给下个玩家发牌。
# 如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌 最终计算并获得每个玩家的分值，

import random

result = {}
user_list = ["alex", "武沛齐", "李路飞"]
# 生成扑克牌
poke_list = []
color = ['黑桃', '红桃', '梅花', '方片']
for x in color:
    for i in range(1, 14):
        poke_list.append((x, i))
poke_list.append(('小王', 14))
poke_list.append(('大王', 15))
print(poke_list, len(poke_list))
a = poke_list
# 随机抽牌，规定分数
for i in user_list:
    print(f'第{user_list.index(i) + 1}位玩家：{i}')
    poke_list = a
    score = 0
    while True:
        index = random.randint(0, len(poke_list) - 1)  # 前后都包括
        if poke_list[index][1] < 11:
            score = score + poke_list[index][1]
        else:
            score = score + 0.5  # 规定分数
        print(poke_list[index])  # 抽到的牌
        poke_list.pop(index)  # 剔除这张牌
        if score > 11:  # 判断爆没爆
            print(f'{score}超过了11，爆掉了')
            print(f'{i}的总分数是：0')
            score = 0
            break
        print(score)  # 展示分数
        question = input('是否继续要牌？y/n')
        if question == 'n':  # 判断是否继续要牌
            print(f'{i}的总分数是：{score}')
            break
        else:
            continue
    result.update({i: score})
print('最终结果如下')
print(result)
