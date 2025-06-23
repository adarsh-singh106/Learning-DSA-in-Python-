class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        self.n=0
    def push(self,value):
        new_node=node(value) # creating New Node
        new_node.next=self.top  # saving the cuu top_node in next of New_node
        self.top=new_node # reassigning the self node
        self.n+=1
    def isempty(self):
        return self.top==None
    def transverse(self):
        curr_top=self.top
        res=""
        while curr_top != None:
            res+=str(curr_top.data)
            curr_top=curr_top.next
        return res
    def peak(self):
        if not self.isempty():
            return self.top.data
        return 'Empty stack'
    def pop(self):
        if not self.isempty():
            data=self.top.data
            self.top=self.top.next
            self.n-=1
            return data
        return 'Empty Stack'
    def size(self):
        return self.n
def bracket_verify(l):
    opening=stack() # Not All Cases Are included 
    for i in range(len(l)):
        a=l[i]
        if a=='(' or a=='{' or a=='[':
            opening.push(a)
        elif a==')' or a=='}' or a==']':
            if a==')' and opening.peak()+a=='()':
                opening.pop()
            elif a==']'and opening.peak()+a=='[]':
                opening.pop()
            elif a=='}'and opening.peak()+a=='{}':
                opening.pop()
            else:
                return "Incorrect use of Brackets"
    if opening.size()==0:
        return "All Brackets Are Properly Used"
    else :
        return "Incorrect use of Brackets"
            
a="{5+[6('x'+'y)'}]"
b=bracket_verify(a)
print(b)
            

