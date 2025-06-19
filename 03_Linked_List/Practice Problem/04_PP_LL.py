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
            result+=str(curr.data)+"->"
            curr=curr.next
        return result[:-2]
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
    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

   # Variable Naming Sucks 
    """def reverse(self):
        curr=self.head
        temp_next=None
        temp_curr=None
        while curr != None:
            temp_next=curr.next
            curr.next=temp_curr
            temp_curr=curr
            curr=temp_next
        # curr.next=temp_curr
        self.head=temp_curr"""


    
L=LinkedList()
L.append_from_head(8)
L.append_from_Tail(-6)
L.append_from_head(1)
L.append_from_Tail(2)
L.append_from_head(40)
L.append_from_Tail(100)
print(L)
L.reverse()
print(L)