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
        while curr_top != None:
            print(curr_top.data)
            curr_top=curr_top.next
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
    
    ############# INSIDE CLASS #####################
    """ correct Logic First Made Stack Of h,e,l,l,o then drived a olleh"""
    # def reverse(self,value):
    #     for i in value:
    #         self.push(i)
    #     result=""
    #     while not self.isempty(): # isempty = true only if stack is empty
    #         temp=s.pop()
    #         result+=temp
    #     return result
    def __sizeof__(self):
        return self.n


    ############# INSIDE CLASS #####################
def reverse(value):
    ass=stack()
    for i in value:
        ass.push(i)
    result=""
    while not ass.isempty(): # isempty = true only if stack is empty
        temp=ass.pop()
        result+=temp
    print(result)
s=stack()
reverse("gandU")
s.push(1)
s.push(5)
s.push(8)
s.push(6)
# s.transverse()

print(s.__sizeof__())
        