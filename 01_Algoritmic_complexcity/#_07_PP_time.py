A=[1,2,3,4]
B=[2,3,4,5]
for i in A:
    for j in B:
        for k in range(100000):
            print('({},{})'.format(i,j))
        

# The Inner Most Loop Is Consatnt 
# Thus O(n)*(n) = O(n**2)