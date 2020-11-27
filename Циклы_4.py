a=int(input())
b=int(input())
k=0

for i in range (a,b+1):
    for j in range (2,i):
        if i%j==0:
            k=k+1
    if k==0:
        print (i)
        k=0
    else:
        k=0
