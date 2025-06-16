def intToStr(i):
    digits =  '0123456789'
    if i==0: 
        return '0'
    result =""
    while i > 0: 
        result = digits[i%10]+ result
        i=i//10
    return result
s=intToStr(int(input("N = ")))
print(s,type(s))
# soulutin 

# input    123  1234  12345

# Loop      3    4      5

# This property Belongs to Log(n)

# Agar Loop Mai chijee Divde hoti ja rahi h Toh , vo generally log(n) ka case hota h