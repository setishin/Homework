n=int(input())
a=[]
k=0
for i in range (n):
    a.append(int(input()))
    
a=a[::-1]

for i in range (len(a)):
    if a[i]==1:
        k=k+1
    if k==2:
        x=i
        break

print (len(a)-x-1)