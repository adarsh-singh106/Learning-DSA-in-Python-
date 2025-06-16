def sum_digit(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10  # chije divide hote ja rahi h 
    return sum
print(sum_digit(int(input("N = "))))

# O(log(n))