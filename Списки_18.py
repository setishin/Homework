import itertools
a=[]
b=[]
c=[]
d=[]
n=int(input())
for i in range(n):
    a.append([j for j in input().split()])
    
b=list(itertools.zip_longest(*a))

for i in range (len(b)):
    for j in range (len(b[i])):
        if b[i][j]!=None:
            c.append (b[i][j])
        else:
            break        
del c[-1]
for i in range (len(b)):
    for j in range (len(b[i])):
        if b[i][j] not in c and b[i][j]!=None:
            d.append (b[i][j])
            
print ()
print (c)
print (d)