def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

n=int(input())
a=[]
b={1, 2, 3, 5, 7, 11, 13, 17, 19}
c=[]
k=[]

for i in range (n):
    a.append(int(input()))

for  i in range (n):
    if a[i] in b:
        c.append (a[i])
    else:
        k=Factor (a[i])
        for j in range (len(k)):
            c.append (k[j])
        
        
print (c)
        
    
