
# a = [ 1,2,3,4,5]
# b = [ 1,2,3,4,5]

# x = zip(a,b)
# print(type(x),type(b))





# a = input("x,y :").split()
# b = input("x,y :").split()
# c = input("x,y :").split()
# x = []

# a = list(map(int,a))
# b = list(map(int,b))
# c = list(map(int,c))
# print(a,b,c)
# if a[0] == b[0] :
#     x.append(c[0])
# elif a[0] == c[0]:
#     x.append(b[0])
# else:
#     x.append(a[0])    
    
# if a[1] == b[1] :
#     x.append(c[1])
# elif a[1] == c[1]:
#     x.append(b[1])
# else:
#     x.append(a[1])    

# print(x)    






# num = int(input("num?"))

# if num == 1 :
#     print(f'{num} is not a prime number')
# elif num > 1:
#     for i in range(2,num):
#         if (num%i) == 0:
#             print(f"{num} is not a prime number \n{i} times {num//i} = {num} ")
#             break
#             # print(f'{i} times {num//i} = {num}')
#     else:
#         print(f'{num} is a prime number')    
# else:
#     print(f'{num} is not a prime number')



# num = int(input("num:"))
# x = True 
# for i in range(2,num):
#     if num%i == 0:
#         x = False
# if x:
#     print("prime") 
# else:
#     print("not a prime number")       




# x = input("enter a letter:")
# if x == x[::-1]:
#     print(f'{x} is palindrome')
# else:
#     print(f'{x} is not palindrome')
# a = input("makan  , esm , meghdar ?").split()



orderList = {
    'm':{},
    'f':{},
    'g':{},
    'k':{}
}

order = input()
while order.lower() != 'exit':
    loc,name,qu = order.split()
    orderList[loc][name]=name
    order = input()

print(orderList)

print(name)