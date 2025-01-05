"""
Write a function that given, an array arr,
returns an array containing at each index i the amount of numbers
that are smaller than arr[i] to the right.
* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]
"""


# arr = [5, 4, 0, 2, 1] - don't need

def smaller(arr):
    n = len(arr)
    low = []
    for i in range(n):
        count_smaller = 0
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count_smaller += 1
        low.append(count_smaller)
    return low


s = smaller([5, 4, 3, 2, 1])
print(s)
