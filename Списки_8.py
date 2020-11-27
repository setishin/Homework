a=input().split()
b=input().split()
c=[]

for i in range (min(len(a),len(b))):
    c.append (a[i])
    c.append (b[i])
    
print (c)
    