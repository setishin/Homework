a=('evgene_o')
b={}
k=0

for i in range(len(a)):
    if a[i] not in b:
        b[a[i]]=1
    else:
        b[a[i]]=b[a[i]]+1
        
c=set('abcdefghijklmnopqrstuvwxyz')

for i in b:
    if i in c:
        k=k+b[i]
        
print (k)