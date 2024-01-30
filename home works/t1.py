x = ["a","e","i","o","u","A","E","I","O","U"]
y = 0
a = input()

for i in a:
    if i in x:
        y = y + 1

if y > 0:
    print(2**y)
else:
    print("1")    
        