print ('введите кол-во строк первой матрицы')
n = int(input()) #кол-во строк первой матрицы
print ('введите кол-во столбцов первой матрицы')
n1=int(input()) #кол-во столбцов первой матрицы

print ('введите первую матрицу')
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
    
print ('введите кол-во строк второй матрицы')    
k = int(input()) #кол-во строк второй матрицы
print ('введите кол-во столбцов второй матрицы')
k1=int(input()) #кол-во столбцов второй матрицы

print ('введите вторую матрицу')
b = []
for i in range(k):
    b.append([int(j) for j in input().split()])
    
c=[[0 for i in range(k1)] for j in range (n)]

for i in range(n):
    for j in range(k1):
        for k in range(n1):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]

print ('Ответ')
print (c)
