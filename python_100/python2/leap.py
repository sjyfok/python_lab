#!/usr/bin/python3
"""
输入年份 判断是不是闰年 如果是输出true
否则生卒乎false
"""
year = int(input('请输入年份: '))
leap = (year%4 == 0 and year % 400 != 0 or year %400 == 0)
print(leap)
