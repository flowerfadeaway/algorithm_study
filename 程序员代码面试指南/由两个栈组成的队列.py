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