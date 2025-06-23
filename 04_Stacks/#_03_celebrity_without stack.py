def celebrity(M):
    n = len(M)
    i = 0
    for j in range(1, n):
        if M[i][j] == 1:
            i = j  # i cannot be celeb, j might be

    # Verify candidate i
    for k in range(n):
        if k != i:
            if M[i][k] == 1 or M[k][i] == 0:
                return "No one is a celebrity"
    return f"The celebrity is {i}"
l=[
    [0,1,1,1],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
]
k=celebrity(l)
print(k)        
        