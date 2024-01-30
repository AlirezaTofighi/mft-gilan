import numpy as np


b,c = tuple(map(int,input().split()))
a = np.random.randint(100 , size=(b,c))



count = 0

for i in range(b): 
    a.append(list(map(int,input().split())))
    # print(a)
for i in range(b): 
    for j in range(c): 
        if j+1 < c  and j-1 >=0 and i +1 < b and i-1 >=0 :
            if a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
                if a[i][j] < a[i-1][j] and  a[i][j] < a[i+1][j]:
                    # print(f"{a[i][j]} , {i} , {j} , ravesh 1  {a[i][j-1]}, {a[i][j+1]} va {a[i-1][j]} , {a[i+1][j]}")
                    count += 1
            if a[i][j] < a[i][j-1] and a[i][j] < a[i][j+1]:
                if a[i][j] > a[i-1][j] and  a[i][j] >  a[i+1][j]:
                    count += 1
                    # print(f"{a[i][j]} , {i} , {j} , ravesh 2  {a[i][j-1]}, {a[i][j+1]} va {a[i-1][j]} , {a[i+1][j]}")
            
print(count)
