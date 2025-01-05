"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:

Sam Harris => S.H
patrick feeney => P.F
"""


def initials(name):
    # Split the name into words and use a list comprehension to get initials
    initials_list = [word[0].upper() for word in name.split()]

    # Join the initials with a dot separator
    return '.'.join(initials_list)


# Example usage:
print(initials("Sam Harris"))  # Output: "S.H"
print(initials("patrick feeney"))  # Output: "P.F"
print(initials("Vita Kovalchuk"))