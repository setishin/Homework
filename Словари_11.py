import random
ri1 = [random.randint(1, 15) for _ in range(30)]

ri1.sort()

b=[]

for i in range (len(ri1)):
    if ri1[i] not in b:
        b.append (ri1[i])
        
print (b)