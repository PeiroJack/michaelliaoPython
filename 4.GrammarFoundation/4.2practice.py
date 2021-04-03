# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出`'xx.x%'`，只保留小数点后1位：

s1 = 72
s2 = 85
name = '小明'
r = (s2 - s1) / s1 * 100

print('中文')

# 方法一 %
print(name + '的提升率为%.1f%%' % r)

# 方法二format

print('{0}的提升率为{1:.1f}%'.format(name, r))

# 方法三f-string

print(f'{name}的提升率为{r:.1f}%')
