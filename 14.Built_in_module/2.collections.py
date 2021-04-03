#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# 验证创建的Point对象是tuple的一种子类：
print(isinstance(p, Point))
print(isinstance(p, tuple))

# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

from collections import deque
# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

from collections import defaultdict
# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 要保持Key的顺序，可以用OrderedDict

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(3)
luod['1']='a'
luod['2']='a'
luod['3']='a'
luod['4']='c'
luod['4']='a'

