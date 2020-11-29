a = []
c=[]
print ('введите количество строк')
n=int(input())
for i in range(n):
    a.append([int(j) for j in input().split()])
    
for i in range (n):
    for j in range (len(a[i])):
        if j==0 or j==len(a[i])-1:
            c.append(a[i][j])
            
print (c)
    