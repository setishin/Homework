x=0
a=input()
k=0
if a=='':
    while a=='':
        a=input()
        
if a=='STOP':
    print ('Program interrupted by user')
    
else:
    while  k==0:
        for i in range(len(a)):
            if ord(a[i])>=ord('a'):
                x=x+1  
        if x==0:
            print ('Too early in the dictionary. Try again!')
            a=input()
            if a=='':
                while a=='':
                    a=input() 
        else:
            k=k+1
    print ('{:_^30}'.format (a))
        

    