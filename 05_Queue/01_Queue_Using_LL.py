# creating Node
class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.n=0

    # IN QUEUE , Insersation occurs from Tail (rear) ONLY
    def enqueue(self,value): # similar to append from tail in LL
        new_node=node(value)
        # CASE-1 : If Queue is Empty
        if self.rear==None:
            self.front=new_node
            self.rear=self.front
        # CASE-2 : If Queue is not Empty , add from tail
        self.rear.next=new_node
        self.rear=new_node
        self.n+=1

    # IN QUEUE , Deletion occurs from Head (Front) ONLY
    def dequeue(self):
        if self.front==None:
            return 'Empty Queue'
        else:
            self.front=self.front.next
            self.n-=1
    def isempty(self): # True for empty and False for Not empty
        return self.front==None
    def front_item_peak(self):
        if self.front==None:
            return "Empty Queue"
        else:
            return self.front.data
    def rear_item_peak(self):
        if self.front==None:
            return "Empty Queue"
        else:
            return self.rear.data
    def size(self):
        return self.n
        
    def transverse(self):
        curr_node=self.front
        for i in range(self.n):
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
q=Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(4)
q.transverse()
# q.dequeue()
# q.transverse()
# q.dequeue()
# q.transverse()
# q.dequeue()
# q.transverse()
# q.dequeue()
# q.transverse()
print("size=",q.size())
print(q.front_item_peak())
print(q.rear_item_peak())