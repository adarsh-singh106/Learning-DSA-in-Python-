def power(num):
    if num<1:
        return 0
    elif num ==1:
        print(1)
        return 1
    else:
        prev=power(num//2)
        curr =prev*2
        print(curr)
        return curr
    
power(33)
# Logic >>> Count Function Call of input
# num = 10 > 10,5,2,1   ---- 4 calls +3
# num = 100 > 100,50,25,12,6,3,1   ---- 7 calls +3
# num = 1000 > 1000,500,250,125,62,31,15,7,3,1   ---- 10 calls  +3

# the input is getting mutiplied but the time is adding , inreasing logartmicly

# O(log(n))