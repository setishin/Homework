a=input()
b=len(a)
c=a[0]

for i in range (2,b+1):
    if b%i==0:
        c=c+a[i-1]
        
print (c)
    