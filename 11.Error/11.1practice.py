# -*- coding: utf-8 -*-

from functools import reduce

def str2num(s):
    # eval()函数用来执行一个字符串表达式，并返回表达式的值。
    return eval(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
