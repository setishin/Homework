from math import *

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    
n=int(input())
a=[]

for i in range (n):
    k=input()
    if is_number(k)==True:
        k=float(k)
        k=ceil(k)
        a.append (k)
    elif k=='True':
        a.append (1)
    elif k=='False':
        a.append (0)
    else:
        a.append (k)
    k=''
    
print (a)