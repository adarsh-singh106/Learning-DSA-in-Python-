class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        self.n=0
    def push(self,value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node
        self.n+=1
    def isempty(self):
        return self.top ==None
    def pop(self):
        if not self.isempty():
            data=self.top.data
            self.top=self.top.next
            self.n-=1
            return data
        return 'Empty LL'
    def peak(self):
        if not self.isempty():
            return self.top.data
        return 'Empty LL'
    def transverse(self):
        curr_top=self.top
        res=""
        for i in range(self.n):
            res+=str(curr_top.data)+"->"
            curr_top=curr_top.next
        return res[:-2]
    def Queue_using_stacks(self,value,fn):
        if fn=='eq':
            s1.push(value)
            s1+=1
            s1.transverse()
        elif fn=='dq':
            if s2.isempty():
                if s1.isempty():
                    return 'Queue is Empty'
                else:
                    element=s1.pop()
                    s1-=1
                    s2.push(element)
                    s2+=1
                    s2.transverse()
            else:
                s2.top=None
                s2.n=0
                element=s1.pop()
                s1-=1
                s2.push(element)
                s2+=1
                s2.transverse()

s1=stack()
s2=stack()
##############################[ MAKE QUEUE WITH THESE TWO STACKS ]#######################################
# properties of queue
# 1. insertion hota h from rare
# 2. deletion hota h from front 
##################### LOGIC #######################
# 1. Tu Ek Stack mai enqueue and Ek Stack mai dequeue

s1.Queue_using_stacks(1,'eq')
s1.Queue_using_stacks(5,'eq')
s1.Queue_using_stacks(7,'eq')
s1.Queue_using_stacks(3,'eq')
print(s1.transverse())
    

    


