import ctypes
class MeraList:
    def __init__(self): # No value is Taken While Creating Object Of Class MeraList
        self.size=1 # self.size is size of array
        self.n=0 # n is no. of element in Arrray i.e Len(array)

        # Create a Array with size = self.size
        self.A=self.make_my_array(self.size)

    # Function - 1
    def make_my_array(self,capacity):
        # Creates A C-Type Array ( Static + refrential ) using based on input capacity
        return (capacity*ctypes.py_object)()

    # Function - 2
    def __len__(self):
        return self.n # n Is the No. of element In List 
    
    # Function - 3
    def append(self,item):
        #######  Check the item , to avoid a type error ####### 
        # check if Array is empty Or Not
        if self.size == self.n :
            # Check the item , to avoid a type error 
            
            # Resize the array with size = self.size*2
            self.resize(self.size*2)
        # Append
        self.A[self.n]=item
        self.n+=1
    #------------------------WRONG-------------------------
    # def resize(self,new_capacity):
    #     # Create array with new capacity and Update the size of array 
    #     self.B=self.make_my_array(new_capacity)
    #     self.size=new_capacity
    #     for item in self.A:
    #         self.B=self.append(item)
    #     self.A=self.B
    def resize(self,new_capacity):
        # Create array with new capacity and Update the size of array
        B=self.make_my_array(new_capacity)
        # Update size of array 
        self.size=new_capacity
        # Copying the elements of A to B 
        for i in range(self.n):
            B[i]=self.A[i]
        # reassign the A
        self.A=B

    # Function - 4
    def __str__(self): # Before Using this You'll Get <__main__.MeraList object at 0x00000280472A7CB0> when use print statement
        # Aise Print Hona Chaiye [1,2,3]
        result=""
        for i in range(self.n):
            result=result+str(self.A[i])+','
        return '[' + result[:-1] + ']'  # result[:-1]  -1 will slice the last element from result

    # Fubctionn - 5
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "IndexError----No Element found At the given Index"
        
    # Function - 6
    def pop(self):
        if self.n <= 0:
            return 'Empty'
        print(self.A[self.n-1])  
        self.n-=1 

    # Function - 7
    def clear(self):
        self.n=0
        self.size=1

    # Function -8
    # def find_give_index(self,item):  ----------------WRONG-------------------
    #     for i in self.A:
    #         if item == i:
    #             return i-1
    #     return 'Item not found'

    def find(self,item):
        for i in range(self.n):
            if item == self.A[i]:
                return i
        return 'Item not found'
    
    # Function - 9

    def insert(self,pos,item):
        # check If Space Is avilable Or not , size is same as no. of element present in that array
        if self.n==self.size:
            self.resize(self.size*2)
        # Shifting of elements to right till pos index
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        # Paste The item at pos
        self.A[pos]=item
        # Inc no. of Elements 
        self.n+=1

    # Function - 10
    def __delitem__(self,pos):
        if 0<= pos < self.n:
            # delitem the item
            for i in range(pos,self.n-1):# pos se n-2 tak chalega loop
                self.A[i]=self[i+1]
            # Last item deleted
            self.n-=1
    
    # Function - 11
    def remove(self,item):
        pos=self.find(item)
        if type(pos)==int:
            #delete
            self.__delitem__(pos)
        else:
            return pos
    
    # Function - 12
    def sort(self): # Using Shifting + insertion  O(n**2)
        for i in range(1,self.n):
            key=self.A[i] # Storing the that element which is supposed to be inserted
            j=i-1 
            while j>=0 and self.A[j] > key: # j ko zero tak chalna h and ye loop tabhi chalega jab
                                            # key se chote elements present ho , key ke peche
                self.A[j+1]=self.A[j]
                j-=1
            self.A[j+1]=key # Insertion of the element
        return self.A
        
    # Function - 13
    def min(self):
        self.sort() # sorting is in the order of asending order
        return self.A[0]
        
    # Function - 14
    def max(self):
        self.sort() # sorting is in the order of asending order
        return self.A[self.n-1]
    
    # Function - 15
    def sum(self):
        
        s=0
        for i in range(self.n):
            s+=self.A[i]
        return s
    
    # Function - 16
    # def extend(self,other):
    #     # for item in range(other):  # Range Only Takes int , In other , a lsit is passed as argument
    #     for item in other:
    #         self.append(int(item))
    #     return self.A
    def extend(self, other):
        m = len(other)  # number of new elements to be added

        # Resize once if needed
        while self.size < self.n + m:
            self.resize(self.size * 2)

        # Copy directly
        for i in range(m):
            self.A[self.n] = other[i]
            self.n += 1



l=MeraList()

l.append(1)
l.append(1)
l.append(3)
# print(l,"---------",len(l))
# print(l[2])
#----------------------------------
# print("Before Pop",l)
# l.pop()
# print("After Pop",l)
#----------------------------------
# print(l)
# print(l.find(3))
#----------------------------------
# print(l)
# l.insert(1,89898)
# print(l)
#----------------------------------
# l.append('asha')
# l.append('ashlz') # >>>>> sorting is done according to Alphabetical Order , uppercase > Lowercase
# l.append('ash')  # >>>> for min & max , returns according to str size
#----------------------------------
# l.append(5)
# print(l)
# print("min  : ",l.min())
# print("max  : ",l.max())
#----------------------------------
# print("sum : ",l.sum())
#----------------------------------
print(l)
a=MeraList()
a=[8,88,888,54,69,25]
l.extend(a)
print(l)






