#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
d = dict(name = 'Bob', age = 20, score=88)
print(pickle.dumps(d))

f = open(r'.\11.IO\dump.txt','wb')
pickle.dump(d, f)
f.close()

f = open(r'.\11.IO\dump.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()