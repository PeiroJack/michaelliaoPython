# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

# a 通过 b 来转移到 c
def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		move(n - 1, a, c, b)
		print(a, '-->', c)
		move(n - 1, b, a, c)


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')