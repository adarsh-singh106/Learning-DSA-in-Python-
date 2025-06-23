# STACKS Using LL
class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None # topmost node
        self.n=0
    def push(self,value):
        new_node=node(value) # creating New Node
        new_node.next=self.top  # saving the cuu top_node in next of New_node
        self.top=new_node # reassigning the self node
        self.n+=1
    def isempty(self):
        return self.top==None
    def len(self):
        return self.n
    def __str__(self):
        curr_top=self.top
        result=""
        while curr_top != None:
            result+=str(curr_top.data)+"->"
            curr_top=curr_top.next
        return result[:-2]
    def peak(self):
        if not self.isempty():
            return self.top.data
        return 'Empty stack'
    def pop(self):
        if not self.isempty():
            self.top=self.top.next
            self.n-=1
        return 'Empty Stack'
############################STRING_REVERAL###################################
    def reversal_all_element(self):
        pass
        
s=stack()
s.push(1)
s.push(5)
s.push(8)
s.push(6)
print(s,"\n",s.peak(),s.len())
s.pop()
print(s,"\n",s.peak(),s.len())