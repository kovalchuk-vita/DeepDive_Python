"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


def high_and_low(numbers):
    # Split the input string into individual number strings

    num_strings = numbers.split()

    # Initialize highest and lowest with the first number
    highest = lowest = int(num_strings[0])

    # Iterate through the remaining numbers
    for num_str in num_strings[1:]:
        num = int(num_str)
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    # Return the result as a formatted string
    return f"{highest} {lowest}"


# Example usage:
print(high_and_low("1 2 3 4 5"))  # Output: "5 1"
print(high_and_low("1 2 -3 4 5"))  # Output: "5 -3"
print(high_and_low("1 9 3 4 -5"))  # Output: "9 -5"