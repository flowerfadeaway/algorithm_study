# 栈和队列

在学习java的一本书上看到，对于面向过程的程序设计中，首先需要考虑的是算法，即想好解决问题的算法，然后再选择方便数据存储的数据结构，实现时空上的优化。

## 设计一个有getMin功能的栈

栈可以用python的列表代替，增，删操作使用append，pop函数来实现，peak方法使用list[-1]来实现。

假设每个时刻调用getMin即可得到栈的最小值，最简单的思路就是：把栈全部倒出来，取Min即可，时间：$O(n)$，空间$O(1)$，但破坏了栈结构，为了防止这个，就需要额外空间记录，空间$O(n)$。

换个思路：每次栈的更新都有内部Min的更新，所以时间$O(1)$，空间$O(n)$

```python
class MyStack(object):
  """一个带有getMin功能的栈"""

  def __init__(self):
    self.stack=[]
    self.Min=[]
  def append(self,item):
    self.stack.append(item)
    if len(self.Min)==0:
      self.Min.append(item)
    else:
      if item<=self.Min[-1]:
        self.Min.append(item)
      else:
        self.Min.append(self.Min[-1])
  def pop(self):
    self.stack.pop()
    self.Min.pop()
  def peak(self):
    return self.stack[-1]
  def getMin(self):
    return self.Min[-1]


```

为了验证结果的正确性，这里写一个验证器。

```python

def validation(arr):
  return min(arr)

import random

while True:
  num=input('输入进行几次比较')
  if num=='0':
    break
  try:
    n = random.randint(1, 1000)
    arr = []
    mystack=MyStack()
    for i in range(n):
      a=random.randint(-1000, 1000)
      mystack.append(a)
      arr.append(a)
    flag=mystack.getMin()==validation(arr)
    if flag:
      pass
    else:
      print(f'结果不一致,n:{n},arr:{arr},第一种结果为：{mystack.getMin()},第二种结果为：{validation(arr)}')
    print(f'{num}次比较完成！')
  except:
    break

```

该方法与书中的方案二一致。方案一的区别在于self.Min的压入更节省空间，但是弹出也更费时间。

## 由两个栈组成的队列
编写一个类，用两个栈实现一个队列，支持队列的基本操作（add，poll，peek）。通过讨论，无论是否使用类内部记忆的自动更新，都不会对这三个方法的时间度更好的改变，所以就不用了。

猜测，如果不需要之前的记录，其实不需要内部记忆的自动更新。

代码：

```python
class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def add(self,item):
        self.stack1.append(item)
    def swap(self,stack1,stack2):
        while stack1!=[]:
            a=stack1.pop()
            stack2.append(a)
    def poll(self):
        self.swap(self.stack1,self.stack2)
        self.stack2.pop()
        self.swap(self.stack2,self.stack1)
    def peek(self):
        self.swap(self.stack1,self.stack2)
        res=self.stack2[-1]
        self.swap(self.stack2,self.stack1)
        return res
```

时间复杂度：$O(n)$，空间复杂度：$O(1)$。写一个小测试：

```python
que=MyQueue()
que.add(1)
que.add(2)
que.add(3)
que.add(4)
que.add(5)
que.add(6)
que.stack1
que.peek()
que.poll()
que.stack1
que.peek()
```

## 如何仅用递归函数和栈操作逆序一个栈

这里是要求只允许对一个栈进行操作，即额外空间复杂度是$O(1)$，这里用栈[5,4,3,2,1]为例解读。

关于递归操作，现在已知的方法就一个，栈顶元素弹出，然后观察最简单的情况，我们希望可以改变元素在栈中的顺序，并且能够成功应用栈空间存储我们想要的元素。这个递归里面包含了另一个递归函数用于在栈的底部加入元素。具体的过程可以通过pdf中的过程看到。

我们形成一下用于写递归的逻辑，定义一个函数$f$，参数为stack（栈），item=None（上层栈弹出的栈顶元素），如果stack为空，那么栈压入item元素。如果栈不为空，那么弹出栈顶元素为top，对stack=stack，item=top调用递归函数，得到当前栈的逆序，然后使用递归函数g用来在栈底加入元素，参数为stack（栈），item（要加入栈底的元素），top=None（上层栈顶部元素），对于这个递归，当栈为空，则直接加入item，否则，弹出栈顶元素为top，对stack=stack，item=item，top=top，调用递归函数g，直观解释为：要在当前栈的栈底加入元素，那么我们弹出一个元素，对栈底加入元素，再把弹出的元素加回来，边界条件空栈时候直接加入保证算法有效。所以大函数f的直观解释为：想要得到一个一个栈的逆序，就要弹出栈顶元素top，然后对栈进行逆序，然后再用g函数在栈底加入元素。具体关于栈之间需要传递什么参数，可以画个图解决。这里也提出一种方便看懂递归流程的图表示法，在pdf后面显示了。

```python
def g(stack,item,top=None):
    if stack==[]:
        stack.append(item)
        return None
    top=stack.pop()
    g(stack,item,top)
    stack.append(top)

def f(stack,item=None):
    if len(stack)==0:
        stack.append(item)
        return None
    top=stack.pop()
    f(stack,top)
    if item==None:
        return None
    g(stack,item,None)


#stack=[5,4,3,2,1]
#f(stack,None)
#stack

#a=[3,4,5]
#g(a,2,None)
#a


while True:
    try:
        stack = list(map(int, input().split()))
        if stack==[]:
            break
        print(f'你输入的栈（第一个元素是栈底）：{stack}')
        f(stack, None)
        print(f'经过逆序之后的栈：{stack}')
    except:
        break

```

由于f函数的每层栈都是依次弹出栈顶元素，然后对于f每层栈中的g函数，g函数的每层栈是和当层栈中元素个数有关系，所以推测时间复杂度为$O(n^2)$。

对比了书中给出的方法，额外空间复杂度和时间复杂度的阶数一样，书中代码的时间较短，并且递归思路更好理解。

按照题目要求实现的方法reverse，逆序一个栈，可以先得到栈的底部元素，并移除，然后逆序栈，然后再压入刚刚弹出的栈底元素，边界条件当栈为空的时候，不需要操作就是逆序了。现在考虑得到一个栈的底部元素并移除，可否通过递归做到，可以。因为现在已知栈中有元素，那么可以弹出一个元素为reslut，然后，得到栈的栈底元素并移除记为last，然后再压回之前的result，返回last即可，边界条件当弹出栈顶元素后，栈为空，那么直接返回result即可。

```python
def getAndRemoveLastElement(stack):
    result=stack.pop()
    if stack==[]:
        return result
    last=getAndRemoveLastElement(stack)
    stack.append(result)
    return last

def reverse(stack):
    if stack==[]:
        return None
    i=getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(i)

stack=[5,4,3,2,1]
reverse(stack)
stack
```

## 猫狗队列
实现一个队列结构，要求队列内有猫类，狗类，然后可以实现add，pollAll，pollDog，pollCat，isEmpty，isDogEmpty，isCatEmpty方法。

最简单的想法是使用一个数组来存储整个数据，就会发现add，pollAll，isEmpty方法是$O(1)$时间，涉及每个类的方法都是$O(n)$时间，因为需要遍历整个数据。对于poll方法，如果是数组那种连续地址，还需要补位，操作相对麻烦，但时间复杂度阶数不变。

考虑有没有更好的办法，就是用两个队列分别存储实现整个数据的形成。思路是这样的，对于猫类队列，只存储一堆数字，数字代表该猫在整个队列是第几个进入的，同样对于狗队列。这种方法实现出来的各个方法都是$O(1)$时间。该方法由各自类的队列形成整个队列的精髓在于，比较猫队列和狗队列的peek值，谁小，则放入整个队列，大的保留，小的被下一个替代，接着比较，直到只剩一个队列有值，全放入即可，然后完成，对于展示整个队列是$O(n)$时间。

```python
class Pet:
    def __init__(self,type):
        self.type=type
    def getPetType(self):
        return self.type
class Dog(Pet):
    def __init__(self,type='dog'):
        super(Dog,self).__init__(type)
class Cat(Pet):
    def __init__(self,type='cat'):
        super(Cat,self).__init__(type)


from collections import deque
import copy

class CatDogQueue:
    def __init__(self):
        self.dogqueue=deque()
        self.catqueue=deque()
        self.count=0
    def add(self,item):
        self.count+=1
        if item.getPetType()=='cat':
            self.catqueue.appendleft(self.count)
        else:
            self.dogqueue.appendleft(self.count)
    def pollAll(self):
        doglast=self.dogqueue[-1]
        catlast=self.catqueue[-1]
        if doglast>catlast:
            self.catqueue.pop()
        else:
            self.dogqueue.pop()
    def pollDog(self):
        self.dogqueue.pop()
    def pollCat(self):
        self.catqueue.pop()
    def isEmpty(self):
        flag=True if len(self.catqueue)==0 and len(self.dogqueue)==0 else False
        return flag
    def isDogEmpty(self):
        flag=True if len(self.dogqueue)==0 else False
        return flag
    def isCatEmpty(self):
        flag=True if len(self.catqueue)==0 else False
        return flag
    def show(self):
        dogqueue=copy.deepcopy(self.dogqueue)
        catqueue=copy.deepcopy(self.catqueue)
        res = []
        while len(dogqueue)!=0 and len(catqueue)!=0:
            doglast=dogqueue.pop()
            catlast=catqueue.pop()
            if doglast<catlast:
                res.append('dog')
                catqueue.append(catlast)
            else:
                res.append('cat')
                dogqueue.append(doglast)
        while len(dogqueue)!=0:
            dogqueue.pop()
            res.append('dog')
        while len(catqueue)!=0:
            catqueue.pop()
            res.append('cat')
        return res


c1=Cat()
c2=Cat()
c4=Cat()
c8=Cat()
c10=Cat()
d3=Dog()
d5=Dog()
d6=Dog()
d7=Dog()
d9=Dog()

cdque=CatDogQueue()
cdque.add(c1)
cdque.add(c2)
cdque.add(d3)
cdque.add(c4)
cdque.add(d5)
cdque.add(d6)
cdque.add(d7)
cdque.add(c8)
cdque.add(d9)
cdque.add(c10)

cdque.show()
cdque.isCatEmpty()
cdque.pollAll()
cdque.show()
cdque.pollDog()
cdque.show()
cdque.show()
cdque.add(d3)
cdque.show()
cdque.pollAll()
cdque.show()
```

## 用一个栈实现另一个栈的排序

对于辅助栈可以指定它的栈顶到栈底的大小顺序，由大到小，或者由小到大。这个方法的精髓是：把目标栈的元素倒入辅助栈，要求辅助栈由栈顶到栈顶由大到小顺序。所以倒入的元素要求越来越大，如果倒入的元素小于辅助栈顶元素，那么辅助栈元素回倒入目标栈，直至要么待定元素大于等于辅助栈顶元素，或者辅助栈为空，那么直接倒入即可，然后进入下一个循环，直到目标栈为空，完成任务。

```python
def f(stack1,stack2):
    '''
    将stack1栈中的元素排序成stack2中栈顶到栈底由大到小排列
    :param stack1:
    :param stack2:
    :return:
    '''
    while stack1:
        a=stack1.pop()
        while stack2 and a<stack2[-1]:
            stack1.append(stack2.pop())
        stack2.append(a)

stack1=[1,3,5,2,6,4]
stack2=[]
f(stack1,stack2)
```

## 生成窗口最大值数组

有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。例如，数组为`[4,3,5,4,3,3,6,7]`，窗口为3:返回结果为`[5,5,5,4,6,7]`。如果数组长度为$n$，窗口大小为$w$,则一共产生$n-w+1$个窗口的最大值。请实现一个函数。

* 输入：整型数组arr，窗口大小为w
* 输出：一个长度为$n-w+1$的数组res，res[i]表示每一种窗口状态下的最大值

思路：如果采用暴力方法，很明显，时间复杂度为$O(nw)$，当$w$比较小的时候，可以当成 $O(n)$ 的时间复杂度，但是当 $w=\frac{n}{2}$ 的时候，时间复杂度就变成了 $O(n^2)$ 。这道题可以感觉到，后面的大数字可以掩盖前面的小数字，但是超过了数组长度就掩盖不住了，这其实就是感觉，灵感，说不大明白，总结起来就是，我们要维护一个数组：

* 里面的数字都是某种窗口状态下的最大值（后面可以知道存下标更好，信息更多）
* 什么时候将会切换到下一个状态，这里用索引来确定

以上是大概的比较模糊的思路，不足以用来实现算法，下面来文字叙述一下这个算法，这里借用一下书上的算法，以后要学会写成这样的算法格式

首先，生成双端队列qmax，qmax中存放数组arr中的下标。

假设遍历到arr[i]，qmax的放入规则为：

* 如果qmax为空，直接把下标i放进qmax，放入过程结束。
* 如果qmax不为空，取出当前qmax队尾存放的下标，假设为`j`。
  * 如果`arr[j]>arr[i]`，直接把下标`i`放进qmax的队尾，放入过程结束
  * 如果`arr[j]<=arr[i]`，把`j`从qmax中弹出，重复qmax的放入规则

假设遍历到arr[i]，qmax的弹出规则是：

* 如果qmax队头的下标等于`i-w`，说明当前qmax队头的下标已过期，弹出当前队头的下标即可。

根据如上的放入和弹出规则，qmax便成了一个维护窗口为w的子数组的最大值更新的结构。

上述过程，每个下标值最多进qmax一次，出qmax一次。所以遍历的过程中进出双端队列的操作是时间复杂度为$O(n)$，整体的时间复杂度也为$O(n)$

其实，算法写出来后，代码已经很好写了

这是我写的代码：

```python3
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
```

显得很不清晰，于是这里借鉴一下书中的代码

```python3
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
```

就很简洁，而且很对应算法，以后争取这样写

下面介绍一下验证算法，就不多解释了，用的暴力验证法，很简单，直接放代码。

```python3
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
```
