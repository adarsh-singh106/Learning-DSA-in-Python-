# Creating Nodes , jab bhi node create hoga toh ek value store hogi + next node ka address
"""So , intially address none hoga"""
class node:
    def __init__(self,value): # Unlike Arrays , here Values is taken as input While creating a object of node
        self.data=value # Single Element Of Node
        self.next=None  # address of Next Node will be stored Here

class LinkedList():

    def __init__(self):
        # Empty LL => 0 Nodes ==> None
        self.head=None  # First Node / Head Node Of LL
        self.n=0 #  No.Of Nodes In LL

    def __len__(self): # MAGIC METHOD , CALL DIRECTLY BY ' len(LL) '
        """ For LL , len(LL) => No. of Nodes"""
        return self.n
    
    def insert_head(self,value):
        # Value Ka New Node Banaunga
        new_node=node(value)
        # Create a Connection With Head of current LL 
        new_node.next=self.head
        # Reassigning The Head Node 
        self.head=new_node
        # Incrementing n
        self.n+=1
    
    def __str__(self): # Traverse Function 
        curr = self.head
        result='' # Declaring Empty str 
        while curr != None:
            result+=str(curr.data)+'->'  # as adding curr.data to an empty str , thus need to convert it into str
            curr=curr.next
        return result[:-2]

    def insert_tail(self,value): # APPEND Function
        # Creating New Node With The Value Either for Empty LL or Existing LL
        new_node=node(value)
        """IF LL Is empty Make The New Node As head"""
        if self.head==None:
            self.head=new_node
            # Incrementing n
            self.n+=1
            return
        # accessing Tail Node One By One
        curr = self.head
        while curr.next != None: # When The Loops Exit curr = none that , address i.e curr.next is none
            curr=curr.next
        # Assigning address of new node to Current Tail node
        curr.next=new_node  # addition of new node at previous node address block
        # Incrementing n
        self.n+=1
    
    #****************************INefficient**********************************
    """def insert_middle(self,value,after):
        # Creating New Node 
        new_node=node(value)
        # finding the Node to Insert
        curr=self.head
        while curr != None:
            if curr.data == after:
                new_node.next=curr.next
                curr.next=new_node
                self.next+=1
                return
            curr=curr.next
        return 'Item Not Found'"""
    #****************************efficient**********************************
    def insert_middle(self, after, value):
        new_node = node(value)
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1  # ✅ Best practice for tracking size
        else:
            return 'Item not found'


    def clear(self): # Make LL , Empty
        # Empty LL => 0 Nodes ==> None
        self.head=None  
        self.n=0

    def delete_from_head(self):
        if self.head==None:
            # LL already Empty
            return 'EmptyList'
        
        # To Delete The curr Head , just make the node right next to head as Head Node
        """Node Right Next to Head is , head.next"""
        self.head=self.head.next # New Head IS Made
        # decrementing The elements 
        self.n-=1

    def delete_from_tail(self):
        if self.head==None:
            # LL already Empty
            return 'EmptyList'
        curr=self.head # Curr = First Node
        # Kya LL mai sirf Ek He node h ???
        if curr.next == None : # HA
            # This Case IS SAme as delete from head 
            self.delete_from_head() # Now Linked List is Empty
            self.n-=1
            return
        # To Delete The curr Tail , just make the tail.next = None, this means Lsdt second Element WIll be New Tail
        """curr != none  ---> Curr Stops At None , and After Loop Completion Curr = none
           curr.next != None  --->  Curr stops At Tail , curr = Tail
           curr.next.next != None  ---> curr Stops At Last second Element , Curr = Last second Node 
        """
        while curr.next.next != None:
            curr=curr.next # Inrement of Loop
        # After Completion Of this Loop Curr = last Second Node
        
        """Make Last second Node's next = none to delete the existence of curr tail """
        curr.next= None
        self.n-=1
        
    def delete_from_middle(self,value):
        # Check - 1 , if the LL is already Empty
        if self.head==None:
            # LL already Empty
            return 'EmptyList'
        # TO Delete Head 
        if self.head.data==value:
            # Call Delete From head
            return self.delete_from_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data==value:
                break
            curr=curr.next
        # 2 cases , 1. Value Mil Gayi And While Break 
        # 2. Value Nhi Mila and curr.next =  none , means I am at Tail
        if curr.next == None:
            return 'item Not Found'
        else:
            curr.next=curr.next.next
            self.n-=1

    # search by value (find) & Returns Its index
    def search_by_value(self,value):
        if self.head==None:
            # LL already Empty
            return 'EmptyList'
        curr=self.head
        index=0
        while curr != None:
            if curr.data==value: # Our curr node has that value , user is searching for
                return index
            curr=curr.next
            index+=1
        # 2 cases , 1. item mila and loop break hogaya  & 2. while loop pura chala and curr = none
        return 'Item Not Found'
        
    # search by Index (find) & Returns Its index
    # def search_by_index(self,value):
    def __getitem__(self,value): # using magic method __getitem__
        if self.head==None:
            # LL already Empty
            return 'EmptyList'
        curr=self.head
        index=0
        while curr != None:
            if index==value: # Our curr node has that value , user is searching for
                return curr.data
            curr=curr.next
            index+=1
        # 2 cases , 1. item mila and loop break hogaya  & 2. while loop pura chala and curr = none
        
        return 'Item Not Found'
        
        


# Creating Object Of Class LinkedList
L=LinkedList()
L.insert_head(8)
# L.insert_head(55)
# L.insert_head(57)
L.insert_tail(7)
L.insert_middle(8,45)
L.insert_head(69)
# print(L)
# L.delete_from_middle(69)
# print(L)
# L.delete_from_middle(7)
# print(L)
# L.delete_from_middle(659)
# print(L)
# L.delete_from_middle(8)
# print(L)
# L.delete_from_middle(45)
# print(L)
# L.delete_from_middle(69)
print(L)
# print("Item at Index=0 is :",L.search_by_index(0)) # Returns Value At Index = 0
# print("Item at Index=1 is :",L.search_by_index(1))
# print("Item at Index=2 is :",L.search_by_index(2))
# print("Item at Index=3 is :",L.search_by_index(3))
# print("Item at Index=4 is :",L.search_by_index(45))
# print("This Value Is At index : ",L.search_by_value(69)) # Returns Index of Value = 69
# print("This Value Is At index : ",L.search_by_value(8))
# print("This Value Is At index : ",L.search_by_value(45))
# print("This Value Is At index : ",L.search_by_value(7))
# print("This Value Is At index : ",L.search_by_value(609))
#*************************Using Indexing Bu Magic Method *******************************
print("Item at Index=0 is :",L[0]) # Returns Value At Index = 0
print("Item at Index=1 is :",L[1])
print("Item at Index=2 is :",L[2])
print("Item at Index=3 is :",L[3])
print("Item at Index=4 is :",L[4])
