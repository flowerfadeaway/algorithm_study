#学习地址
#https://blog.csdn.net/brucewong0516/article/details/84025027

import queue

q=queue.Queue(5)    #如果不设置长度,默认为无限长
print(q.maxsize)    #注意没有括号
q.put(123)
q.put(456)
q.put(789)
q.put(100)
q.put(111)
q.put(233)
print(q.get(2))
print(q.get())
q.qsize()
q.empty()


#deque更好用
#https://docs.python.org/zh-cn/3/library/collections.html#deque-objects

