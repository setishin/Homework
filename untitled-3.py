n= int(input())
k=1
for i in range (1,n+1):
    k=k*n
    if n-2<1:
        break
    else:
        n=n-2
    
print (k)
    