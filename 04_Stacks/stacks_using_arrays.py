# Arrays implementation in Stacks
class stack:
    def __init__(self,size):
        self.top=-1 # in  LL top is topmost node , here it is index of item in array
        # initially -1 , when added one element, sef.top act  as index of that element i.e 0
        self.size=size
        self.stack=[None]*self.size
        self.n=0 # No. of Elements presentin Array 
    def push(self,value):
        if self.n==self.size: # self.top == self.size-1
            return 'OverFlow'
        else:
            self.top+=1
            self.stack[self.top]=value
            self.n+=1
    def transverse(self):
        for i in range(self.n):
            print(self.stack[i],end=" ")
    def pop(self):
        if self.top == -1 :# stack is empty
            print("Stack is Empty")
        data=self.stack[self.top]
        self.top-=1
        self.n-=1
        print("\nPoped item = ",data)
l=stack(5)
l.push(1)
l.push(2)
l.push(3)
l.transverse()
l.pop()
l.transverse()
l.pop()
l.transverse()
l.pop()
l.transverse()
l.pop()
l.transverse()
