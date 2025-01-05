"""
Write a Python program to iterate through all elements in an array.
"""
def iterate():
    arr = [1, 4, 5, 6, 2, 8]
    for i in arr:
        print (i, end = ' ')


iterate()

def iterate1():
    arr = [1, 4, 5, 6, 2, 8, 100, 67]
    print('\n___________________________\n')
    for i in range(len(arr)):
        print(arr[i], end = ' ')

iterate1()

def iterate2():
    arr = [3, 54, 5, 35, 8, 100, 67]
    print('\n___________________________\n')
    iterator = iter(arr)
    i = 0
    while i < len(arr):
        el = next(iterator)
        i += 1
        print(el, end = ' ')

iterate2()