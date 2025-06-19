# Given a Linked list of charaters. Write a python function to return a new string that is created by
# appending all the characters given in the linked list aå per the rules given below.

# Rules ->
# Replace '* or '/' by a single space
# In case of two consecutive occurrences of '*' or '/' , replace those two occurrences by a single space and
# convert the next character to upper case

# Assume that ->
# There will not be more than two consecutive occurrences of '*' or '/'
# The linked list will always end with an alphabet

# Sample Input
# A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y
# Expected Output
# An Apple a day Keeps A Doctor Away

class node :
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
    def __str__(self):
        result=""
        curr=self.head
        while curr != None:
            result+=str(curr.data)
            curr=curr.next
        return result
    def append_from_head(self,value):
        new_node=node(value) # New_node with Given Value is Created 
        '''To append Node from head , Just make the new Node as head &
        and that can be done by saving old head in new node's address(next)
        '''
        new_node.next=self.head
        # Re-assigning Head
        self.head = new_node
        # Inrement of n
        self.n+=1

    def append_from_Tail(self,value):
        new_node=node(value)
        # if head is already Empty i.e self.head = None
        if self.head == None :
            # LL is Empty # No head Is present
            self.head=new_node
            # increment of n
            self.n+=1
            return 
        # If LL Is not Empty then 
        curr= self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        # increment of n
        self.n+=1
        # def append_in_middle(self):
        #     pass
    def char_change(self):
        curr=self.head
        while curr != None:
            if curr.data == '*' or curr.data == '/':
                curr.data=' '
                if curr.next.data == '*' or curr.next.data == '/':
                    curr.next.next.data=curr.next.next.data.upper()
                    curr.next=curr.next.next # skipped one node # OG LOGIc 
            curr=curr.next
    
L=LinkedList()
L.append_from_Tail('*')
L.append_from_Tail('*')
L.append_from_Tail('t')
L.append_from_Tail('h')
L.append_from_Tail('e')
L.append_from_Tail('/')
L.append_from_Tail('s')
L.append_from_Tail('k')
L.append_from_Tail('y')
L.append_from_Tail('*')
L.append_from_Tail('i')
L.append_from_Tail('s')
L.append_from_Tail('/')
L.append_from_Tail('*')
L.append_from_Tail('b')
L.append_from_Tail('l')
L.append_from_Tail('u')
L.append_from_Tail('e')
print(L)
L.char_change()
print(L)