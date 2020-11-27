a=input()
b=[]
s=''
j={'s','S'}

for i in range (len(a)):
    if not (a[i] in j) or i==0 or i==len(a)-1:
        b.append(a[i])
    else:
        s=a[i-1]+a[i-1]+a[i+1]
        b.append(s)
        s=''

    
print (b)