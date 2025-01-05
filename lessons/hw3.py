
l = [3,5,6,1,4]
for i in l:
    print(float(i))

#Fibbonachi
# n = int(input("Enter length of Fibonacci series: "))
# num1 = 0
# num2 = 1
# next_number = 0
# count = 1
# while (count <= n):
#     print(next_number, end=" ")
#     count += 1
#     num1 = num2
#     num2 = next_number
#     next_number = num1 + num2

#Factorial
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)