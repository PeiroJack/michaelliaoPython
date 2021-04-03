# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

sorted([36, 5, -12, 9, -21])
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'])
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# 练习：
# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
	return t[0].lower()


L2 = sorted(L, key=by_name)

print(L2)


# 再按成绩从高到低排序：
def by_socre(t):
	return t[1]


L2 = sorted(L, key=by_socre, reverse=True)

print(L2)
