# Fibonaci series 
import time
start=time.time()
def fab(n):
    if n ==1 or n==0:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(int(input("Enter a Number :"))))
print(time.time()-start)

# 3 >( 2 > (1 + 0) +1  ) >>> 4
# 5 > (4 > (3 >(2 > (1+0)+1)+2)+3 > (2 > (1+0)+1))  >>> 15

# O( <(2**n) )

############################## WRONG #########################
# Fibonaci series Efficient Version
import time
start=time.time()
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(int(input("Enter a Number :"))))
print(time.time()-start)
