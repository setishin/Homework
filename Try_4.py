def diag (m, main=True):
    for i in m:
        if len (i)!=len(m):
            raise ValueError
        
    s=0
    if main:
        for i,j in enumerate(m):
            s=s+j[i]
    else:
        for i,j in enumerate(m):
            s=s+j[-(i+1)]
    return s

a=[[10,20,3],[4,5,6],[7,8,9]]
print (diag (a))