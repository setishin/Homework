s1=input()
s2=input()
a=[]

if s1<s2:
    k=1
else:
    k=0
    
a.append (s1)
a.append (s2)
a.append (len(s1))
a.append (len(s2))
a.append (k)

print ('������� output')
x=input()

if x=='lengths':
    print ('����� �����',a[2],' ',a[3])
if x=='order' and k==0:
    print ('������', s1, ' ���� ����� ������ ', s2)
if x=='order' and k==1:
    print ('������', s2, ' ���� ����� ������ ', s1)