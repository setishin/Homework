print ('������� ���-�� ����� ������ �������')
n = int(input()) #���-�� ����� ������ �������
print ('������� ���-�� �������� ������ �������')
n1=int(input()) #���-�� �������� ������ �������

print ('������� ������ �������')
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
    
print ('������� ���-�� ����� ������ �������')    
k = int(input()) #���-�� ����� ������ �������
print ('������� ���-�� �������� ������ �������')
k1=int(input()) #���-�� �������� ������ �������

print ('������� ������ �������')
b = []
for i in range(k):
    b.append([int(j) for j in input().split()])
    
c=[[0 for i in range(k1)] for j in range (n)]

for i in range(n):
    for j in range(k1):
        for k in range(n1):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]

print ('�����')
print (c)
