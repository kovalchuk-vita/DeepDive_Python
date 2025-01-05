"""
Take three numbers from the user and print the greatest number.
"""

def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

# Taking three numbers as input from the user
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    # Finding the greatest number
    greatest = find_greatest(number1, number2, number3)
    print(f"The greatest number is: {greatest}")

except ValueError:
    print("Please enter valid numbers")

#______________________________________________
numbers = []

# Use a while loop to take three numbers from the user
while len(numbers) < 3:
    num = int(input("Enter a number: "))
    numbers.append(num)

greatest = numbers[0]

# Find the greatest number using a for loop
for num in numbers:
    if num > greatest:
        greatest = num

# Print the greatest number
print("The greatest number is:", greatest)
