import os.path
import time
import json


def log(*args, **kwargs):
    # time.time() 返回 unix time 转换为可以看懂的格式
    fmt = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(fmt, value)
    with open('xue.log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
