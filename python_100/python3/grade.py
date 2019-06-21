#!/usr/bin/python3
#一定要放在首行

'''
百分制等级
90-100  : A
80-89   : B
70-79   : C
60-69   : D
0-59    : E
'''

score = float(input('请输入程序: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('对应的等级是:', grade)
