#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# task_worker.py
'''
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# Create QueueManager
class QueueManager(BaseManager):
    pass

def do_task_work():
    # This QueueManger can only acquire Queues from network, so only name provided
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # Connect to server where task_master.py is running
    server_addr = '127.0.0.1'
    print('Connect to server %s ...' % server_addr)

    # authkey must be coordinated with task_master.py
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # Connect to network
    m.connect()

    # Acquire queue objects
    task = m.get_task_queue()
    result = m.get_result_queue()

    # Read task from task_queue and write to result to result_queue
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('Task queue is empty.')

    # All work done
    print('worker exit')

if __name__ == '__main__':
    do_task_work()