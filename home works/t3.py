n ,x = input().split()
y , z = [] ,[]
for i in x:
    z.append(i)
z = set(z)
for i in range(int(n)):
    b = input()
    y.append(b)
for char in y:
    g= []
    for j in char:
        g.append(j)     
    g = list(set(g))
    if sorted(g) == sorted(z):
        print("Yes")
    else:
        print("No")
        




