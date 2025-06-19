# Creating Nodes , jab bhi node create hoga toh ek value store hogi + next node ka address
"""So , intially address none hoga"""
class node:
    def __init__(self,value): # Unlike Arrays , here Values is taken as input While creating a object of node
        self.data=value # Single Element Of Node
        self.next=None  # address of Next Node will be stored Here

a=node(5)
b=node(5884)
print(a) # Gives address Of that object , Unless You Have Used magic __str__() meethod
"""But But But, here's How You Can Print The Attribute OF Your Object """
print(a.data)
print(a.next)
print(b.data)
print(b.next)

