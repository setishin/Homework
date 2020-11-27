max_val=10
repeat=int(input())
x=[]
a=[]
b=[]
c=[]
d=[]

for i in range (1,max_val+1):
    x.append (i)
    
x=x*repeat
k=len(x)
a=x
b=a[:k//5]
c=a[-k//5:]
d=b+c

for i in range (len(a)):
    if a[i] not in d:
        a[i]=a[i]*10

print (a)        
print (d)