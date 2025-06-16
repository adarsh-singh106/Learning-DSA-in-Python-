L = [1,2,3,4,5]
for i in L:# O(n)
    for j in L: # O(n)
        print('{},{}'.format(i,j))

# net order = O(n) * O(n) = O(n**2)
# Quadratic