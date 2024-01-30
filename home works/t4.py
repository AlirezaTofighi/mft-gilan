z = input().split()
a = int(z[0])
b = int(z[1])


for i in range(a):
    print(" _"*b)

    for j in range(b+1):
        print("| ",end = '')
    print()
print(" _"*b) 
