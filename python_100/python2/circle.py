#!/usr/bin/python3
"""
输入圆的半径 计算面积和周长
S = PI*R*R
L = PI*2*R
导入数学库 并且应用pi变量
"""
import math
#PI = 3.14;
R = float(input('请输入度半径: '))
S = math.pi*R*R;
L = 2*math.pi*R;
print('面积=%.2f， 周长 = %.2f' %(S, L))
