class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def push(self,value):
        new_node=node(value) # creating New Node
        new_node.next=self.top  # saving the cuu top_node in next of New_node
        self.top=new_node # reassigning the self node
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
            return data
        return 'Empty Stack'
    

    """ correct Logic First Made Stack Of h,e,l,l,o then drived a olleh"""
def reverse(value):
    ass=stack()
    for i in value:
        ass.push(i)
    result=""
    while not ass.isempty(): # isempty = true only if stack is empty
        temp=ass.pop()
        result+=temp
    print(result)

def text_edit(value,pattern):
    ash=stack()
    serena=stack()
    for i in value:
        ash.push(i)
    for i in pattern:
        if i=='u':
            serena.push(ash.top.data)
            ash.pop()
        elif i == 'r':
            ash.push(serena.top.data)
            serena.pop()
        else:
            return 'Invalid Char In pattern'

    return reverse(ash.transverse())

            

s=stack()
# print(s.reverse('gand'))
# s.push(1)
# s.push(5)
# s.push(8)
# s.push(6)
# s.transverse()
print(text_edit('ashu','uur'))