from random import *
a={}
i=1
while True:
    x=input()
    if x=='':
        print (a)
        break
    elif (len(a)<5) and (x not in list(a.values())):
        a[i]=x
        i=i+1
    elif x in list(a.values()):
        print ('“акое значение уже есть в мешке!')
    else:
        k=randint (1,5)
        print ('удал€емое значение', a[k])
        del (a[k])
        a[k]=x