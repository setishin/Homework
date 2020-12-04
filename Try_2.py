def multiply (a):
    res=1
    try:
        for i in range (len(a)):
            res=res*float(a[i])
        return res
    except ValueError:
        raise ValueError

k=input().split()
print (multiply (k))