a=list(input())
d1 = {'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10}
k=0

for i in a:
    if i in d1:
        k=k+1
        
print (k)