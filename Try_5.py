def treug (a1,a2,a3):
    assert (a1[1]-a2[1])*a3[0]+(a2[0]-a1[0])*a3[1]+(a1[0]*a2[1]-a2[0]*a1[1])!=0, 'Невозможно задать треугольник'
    return (abs((a2[0]-a1[0])*(a3[1]-a1[1])-(a2[1]-a1[1])*(a3[0]-a1[0])))/2

x1=int(input())
y1=int(input())
a=[]
a.append (x1)
a.append (y1)
a=tuple(a)

x2=int(input())
y2=int(input())
b=[]
b.append (x2)
b.append (y2)
b=tuple(b)

x3=int(input())
y3=int(input())
c=[]
c.append (x3)
c.append (y3)
c=tuple(c)

print (treug(a,b,c))