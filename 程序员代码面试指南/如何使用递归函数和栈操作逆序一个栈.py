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