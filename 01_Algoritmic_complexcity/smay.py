import time
start=time.time()
#i=1
# alogoritm /Logic 1
for i in range(101):
    print(i)
# # alogoritm /Logic 2
# while i<101:
#     print(i)
#     i+=1
# alogoritm /Logic 3
# while i<=100:
#     print(i)
#     i+=1
print(time.time()-start)


# Conclusion Why this Is Not Used in Industry
# 1. Every time You Run The Program It gives different Time 
# 2. Same code / Logic Will Take Different Time On Different Hardware
# 3. though Logic is same , making Slight Changes In code , time Changes
# 4. So, Ultimaetly , we cant find relation Between time and code(INPUT) , when changed input