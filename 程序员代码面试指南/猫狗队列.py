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