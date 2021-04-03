# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

def findMinAndMax(L):
    if len(L) ==0:
        return (None, None)
    Max = Min = L[0]
    for value in L:
        if value > Max :
            Max = value
        if value < Min :
            Min = value
    return (Min, Max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')