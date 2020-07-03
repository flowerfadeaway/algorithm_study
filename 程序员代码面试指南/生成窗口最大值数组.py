from collections import deque

arr=list(map(int,input().split()))
w=int(input())

n=len(arr)
dq=deque(maxlen=w)
#dq.append(0)
res=[]


for i in range(1,n):
    if i==0:
        dq.append(0)
        #continue
    if i-dq[0]>=w:
        dq.popleft()
    while len(dq)>0 and arr[i]>=arr[dq[-1]]:
        dq.pop()
    dq.append(i)
    #下面的语句单纯为了符合本题的输出格式而定制
    if i>=w-1:
        res.append(arr[dq[0]])

print(f"窗口最大值数组为：{','.join(map(str,res))}")

def f1(arr,w):
    n = len(arr)
    dq = deque(maxlen=w)
    #dq.append(0)
    res = []

    for i in range(0, n):
        if i == 0:
            dq.append(0)
            #continue
        if i - dq[0] >= w:
            dq.popleft()
        while len(dq) > 0 and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        # 下面的语句单纯为了符合本题的输出格式而定制
        if i >= w - 1:
            res.append(arr[dq[0]])
    return ','.join(map(str, res))
    #print(f"窗口最大值数组为：{','.join(map(str, res))}")

##############
#这里写一个暴力验证方案
##############

from collections import deque

arr=list(map(int,input().split()))
w=int(input())

n=len(arr)
dq=deque(maxlen=w)
#dq.append(0)
res=[]

for i in range(0,n):
    if i <= w-1:
        dq.append(arr[i])
    if i == w-1:
        res.append(max(dq))
    if i >=w:
        dq.append(arr[i])
        res.append(max(dq))
print(f"暴力法得到的窗口最大值数组为：{','.join(map(str,res))}")

def f2(arr,w):
    n = len(arr)
    dq = deque(maxlen=w)
    # dq.append(0)
    res = []

    for i in range(0, n):
        if i <= w - 1:
            dq.append(arr[i])
        if i == w - 1:
            res.append(max(dq))
        if i >= w:
            dq.append(arr[i])
            res.append(max(dq))
    #print(f"暴力法得到的窗口最大值数组为：{','.join(map(str, res))}")
    return ','.join(map(str, res))

##############
#验证程序
##############

import random
#random.randint(0,1000)
arr=[]
for i in range(100):
    for j in range(20):
        arr.append(random.randint(0,1000))
    w=random.randint(1,10)
    s1=f1(arr,w)
    s2=f2(arr,w)
    if s1!=s2:
        print(f'出现了两个方法不一致,arr:{arr};w:{w}')
        break


####################
#书中
####################
from collections import deque
def getMaxWindow(arr,w):
    if arr==None or w<1 or len(arr)<w:
        return None
    qmax=deque()
    res=[0 for _ in range(len(arr)-w+1)]
    index=0
    for i in range(len(arr)):
        while len(qmax)>0 and arr[qmax[-1]]<=arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0]==i-w:
            qmax.popleft()
        if i>=w-1:
            res[index]=arr[qmax[0]]
            index+=1
    return res