a=input()
b=input()
c=''
for i in a:
    if i in b and i not in c:
        c=c+i
        
print (c)

    