"""
Write a Python program to print all the elements of an Array using the position of the elements.
"""

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(array)):
    print(f"Position {index}: {array[index]}")

print('\n___________________________\n')

array = [10, 20, 30, 40, 50]
for index, value in enumerate(array):
    print(f"Position {index}: {value}")