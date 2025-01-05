# l1 =[]
# l2=[]
# l3=[]
# for i in range(1,10):
#     if i % 2 == 0:
#         l1.append(i)
#     elif i % 3 == 0:
#         l2.append(i)
#     elif i%2 >= 1 and i%3>=1:
#         l3.append(i)
# print('Even numbers:',l1)
# print('Odds numbers:',l2)
# print('Not even, not odds numbers:',l3)

count = 0
while count < 3:
    login = input('Enter your login: ')
    if login == 'Qwerty':
        print("Success access!")
        break
    else:
        print("Invalid login. Try again, please ")
        count += 1
print('You used 3 tries')