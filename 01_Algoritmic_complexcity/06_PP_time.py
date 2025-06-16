# O(AB)


A = [1,2,3,4]
B = [2,3,4,5,6]
for i in A:
    for j in B:
        if  i<j:
            print('{},{}'.format(i,j))