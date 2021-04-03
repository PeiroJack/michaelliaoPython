#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# 这里因为windows是需要用gbk来解码
# print(output.decode('utf-8'))
print(output.decode('gbk'))
print('Exit code:', p.returncode)
