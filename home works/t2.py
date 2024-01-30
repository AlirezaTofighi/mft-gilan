n = int(input())
b=[]

for i in range(n):
    a = input()
    b.append(a)
for i in b:
    if not i.isdigit() :
        print(i.title())



