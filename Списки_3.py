a=['input','string','repeat',3]
if 'repeat' in a and type(a[-1])==int:
    b=a[:-2]*a[-1]+a[-2:]
    
print (b)
 
   