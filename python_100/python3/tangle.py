#!/usr/bin/python3
#一定要放在首行

'''
输入三角形的三条边
如果能构成三角形 输入其面积周长
否则提示不能构成3角形
'''

import math
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

if a+b > c and a+c > b and b+c > a :
    print('周长: %f' %(a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积:%f' %(area))
else:
    print('不能构成三角形')


