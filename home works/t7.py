x,y,z = tuple(map(int,input().split()))
matrix1 =[]
matrix2 =[]
for _ in range(x):
    matrix1.append(list(map(int,input().split())))
    
for _ in range(y):
    matrix2.append(list(map(int,input().split())))

row1 = len(matrix1)
row2 = len(matrix2)
col1 = len(matrix1[0])
col2 = len(matrix2[0])

result = []
for i in range(row1):
    row = []
    for j in range(col2):
        row.append(0)
    result.append(row)

for i in range(row1):
    for j in range(col2):
        for k in range(col1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    row_str = " ".join(map(str, row))
    print(row_str)