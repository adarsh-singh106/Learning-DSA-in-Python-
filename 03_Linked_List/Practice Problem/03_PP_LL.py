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
    def even_sum(self):
        index=0 # starting Indexing
        sum=0 # Will store sum of OddIndex here
        curr=self.head 
        while curr != None:
            if index%2 == 0:
                sum+=curr.data
            index+=1
            curr=curr.next
        return sum
    
    def odd_sum(self):
        index=0 # starting Indexing
        sum=0 # Will store sum of OddIndex here
        curr=self.head 
        while curr != None:
            if not index%2 == 0:
                sum+=curr.data
            index+=1
            curr=curr.next
        return sum
    
L=LinkedList()
L.append_from_head(8)
L.append_from_Tail(-6)
L.append_from_head(1)
L.append_from_Tail(2)
L.append_from_head(40)
L.append_from_Tail(100)
print(L)
print(L.odd_sum())
print(L.even_sum())