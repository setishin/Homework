n=int(input())
a=[]
b=[]
k=0
for i in range (n):
    a.append(int(input()))
    
m=min(a)
k=a.count(m)
x=a.index(m)

if k==2:
    print (x)
elif k>2:
    print ('Такого значения  нет')
else:
    for i in range (n):
        if a[i]!=m:
            b.append(a[i])
    p=min(b)
    print (a.index(p))