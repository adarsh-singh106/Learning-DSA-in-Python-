# Time Efficiency In Recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(int(input("Enter a Number :"))))

 # Logic Is Just like It was in Loops 
 # Focus On No. of time Function Is called

#  5! >>> 5 Fn calls
#  10! >>> 10 Fn calls
#  100! >>> 100 Fn calls

# order O(n) i.e Liner