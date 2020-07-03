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