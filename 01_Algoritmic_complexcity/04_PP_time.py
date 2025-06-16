#---------------INCORRECT-----------------
'''n=10
k=0
for i in range(int((n/2)+1)):
    j=2
    while j<=n:
        k=k+n/2
        j*=2'''
#---------------CORRECT-----------------
n = 10
k = 0

for i in range(n // 2, n + 1): # O(n)     # i from 5 to 10 (6 iterations)
    j = 2
    while j <= n:   # O(log(n))           # j = 2, 4, 8 (3 iterations)
        k = k + n // 2         # k += 5
        j *= 2
print("k =", k)
# As these are nested Loop thus There Will Be Multiplication 
# >>>>>>>>>>>
# O(n)*O(log(n)) = O(nLog(n))

# n = 10
# k = 0

# for i in range(n // 2, n + 1):
#     j = 2
#     while j <= n:
#         k = k + n // 2
#         j = j * 2

# print("Final value of k:", k)
