a=int(input())
b=int(input())
x=[]

for i in range (a,b+1):
    if i <= 1:
        continue
    for j in range (2,i//2+1):
        if i%j==0:
            break
    else:
        x.append (i)
        
print (x)
