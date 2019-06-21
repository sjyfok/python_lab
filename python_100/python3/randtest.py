#!/usr/bin/python3
#一定要放在首行

'''
应用随即数来模拟掷骰子
'''

from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱歌'
elif face == 2 :
    result = '跳舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '将冷笑话'
print(result)
