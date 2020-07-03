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


