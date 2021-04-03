#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# task_master.py
'''
import random, time, queue
from multiprocessing.managers import BaseManager
# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

#在win10环境下，pickle模块不能序列化lambda函数，所以需要自定义要使用的函数，而不用lambda函数
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    #QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_task_queue', callable=return_result_queue)
    #QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random, time, queue
from multiprocessing.managers import BaseManager

# Queue for send tasks
task_queue = queue.Queue()
# Queue for accept results
result_queue = queue.Queue()

# Create a QueueManager herited from BaseManager
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue

def getresult():
    return result_queue

def do_task_master():
    # Register the two queues to network, argument callable references to Queue object
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)

    # When run under windows, it not support bind through lambda
    QueueManager.register('get_task_queue', callable=gettask)
    QueueManager.register('get_result_queue', callable=getresult)

    # Bind port to 5000, set authentication code as 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # Start queue
    manager.start()

    # Acquire Queue that used to access through network
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # Put some tasks into task Queue
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # Read result from result queue
    print('Try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('Result Queue is empty')

    # Close
    manager.shutdown()
    print('Master exit')

if __name__ == '__main__':
    do_task_master()