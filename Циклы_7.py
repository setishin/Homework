a=input()
c=input()
b=c.lower()
p=''

for i in range (len(a)):
    if a[i].lower() or a[i] in b:
        k=i+1
        for j in range(len(b)):
            if b[j]==a[i] or b[j]==a[i].lower():
                p=b[j].upper()
                b=b[:j]+p+b[j+1:]
        if  not(b.islower()):    
            print (k,'ñèìâîë âñòðå÷àåòñÿ â ñòðîêå ïîèñêà:',b)
            b=b.lower()
            
        
        
        
