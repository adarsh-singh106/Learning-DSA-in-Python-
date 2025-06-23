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
    
l=[
    [0,1,1,1],
    [0,0,0,0],
    [0,1,0,0],
    [0,1,1,0],
]
def celebrity(matrix_n):
    cel=stack()
    for item in range(len(matrix_n)):
        cel.push(item)
    while cel.size() >=2:
        z=cel.pop()
        y=cel.pop()
        if matrix_n[z][y]==1: # z is not celebrity , coz celebrity vo h jo kisi ko nhi jaanta
            cel.push(y)
        elif matrix_n[z][y]==0: 
            cel.push(z)
        else:
            return 'Invalid Matrix'
    celb= cel.pop()
    for i in range(len(matrix_n)):
        if i!=celb:
            if matrix_n[i][celb]==0 or matrix_n[celb][i]==1:
                return "No on is celebrity"
    return f"The celebrity is {celb}"
k=celebrity(l)
print(k)        
        



    
