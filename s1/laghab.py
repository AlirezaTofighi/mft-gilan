laghab = ['Haji' , 'Karbalaee' , 'Mashti' , 'Agha']
a = input()
b = []

for i in a:
    b.append(i)
    
if b[0] == 'Y'  :
    print(laghab[0])
elif b[1] == 'Y'  :
    print(laghab[1])    
elif b[2] == 'Y': 
    print(laghab[2])   
else :
    print(laghab[3])    