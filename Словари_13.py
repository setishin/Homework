a=('evgene_o00000000')
b={}

for i in range(len(a)):
    if a[i] not in b:
        b[a[i]]=1
    else:
        b[a[i]]=b[a[i]]+1
        
for i,j in list(b.items()):
    if j<5:
        del b[i]
        
print (b)