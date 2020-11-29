a=('evgene_o')
b={}

for i in range(len(a)):
    if a[i] not in b:
        b[a[i]]=1
    else:
        b[a[i]]=b[a[i]]+1
        
print (b)