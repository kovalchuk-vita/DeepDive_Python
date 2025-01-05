'''Description
You have clothes international size as text (xs, s, xxl).
Your goal is to return European number size as a number from that size .

Notice that there is arbitrary amount of modifiers (x), excluding m size, and input can be any string.

Linearity
Base size for medium (m) is 38.
(then, small (s) is 36, and large (l) is 40)

The scale is linear; modifier x continues that by adding or subtracting 2 from resulting size.

Invalid cases
Function should handle wrong/invalid sizes.

Valid input has any base size (s/m/l) and any amount of modifiers (x) before base size (like xxl).
Notice that you cannot apply modifier for m size, consider that case as invalid!
Anything else is disallowed and should be considered as invalid (None for Python, 0, false for Go, null for JavaScript).

Invalid examples: xxx, sss, xm, other string

Valid Examples xs: 34 s: 36 m: 38 l: 40 xl: 42
'''


# class InvalidSizeError(Exception):
#     pass
#
#
# def size_to_number(size):
#     base_sizes = {
#         's': 36,
#         'm': 38,
#         'l': 40
#     }
#
#     if not isinstance(size, str) or not size:
#         raise InvalidSizeError("Invalid size input: must be a non-empty string")
#
#     size = size.lower()
#
#     # Extract base size and modifier part
#     base_size = None
#     modifier_count = 0
#
#     # str = 'xxxl' 's'
#     # str[:-1] #--> xxx
#     #
#     # # Error Case base needs to be at the end
#
#     #if not size or size[-1] not in base_sizes: return None
#     if size[-1] not in base_sizes: return None #lx, xlx, nm
#
#     for char in size:  # 'xxs' 'xsx'
#         if char == 'x':
#             modifier_count += 1
#         elif char in base_sizes:  # ss
#             if base_size is None:
#                 base_size = char
#             else:
#                 # More than one base size character is invalid
#                 raise InvalidSizeError("Invalid size input: multiple base size characters") #lxl, mm
#         else:
#             # Invalid character
#             raise InvalidSizeError("Invalid size input: contains invalid characters") #nm
#
#     if base_size not in base_sizes:
#         raise InvalidSizeError("Invalid size input: base size character not found")
#
#     if base_size == 'm' and modifier_count > 0:
#         raise InvalidSizeError("Invalid size input: medium size cannot have modifiers")
#
#     if len(base_size) != 1:  # base size contains 1 character 's', not sss
#         raise InvalidSizeError("Invalid size input: multiple base size characters")
#
#     # Calculate the European number size
#     base_number = base_sizes[base_size]  # 34
#     if base_size == 's':
#         return base_number - (modifier_count * 2)
#     elif base_size == 'l':
#         return base_number + (modifier_count * 2)
#     else:
#         return base_number
#
#
# def main():
#     while True:
#         try:
#             user_input = input("Enter the international size or 'q' to exit: ")
#             if user_input.lower() == 'q':
#                 break
#             result = size_to_number(user_input)
#             print(f"European size: {result}")
#         except InvalidSizeError as e:
#             print(f"Error: {e}")
#
#
# main()

#________________________________________

# def size_to_number(size):
#     base_sizes = {'s': 36, 'm': 38, 'l': 40}
#     current_letter = 0
#     if len(size) >= 1:
#         if len(size) == 1:
#             return base_sizes.get(size[current_letter], None)
#         last_letter = size[-1]
#         if last_letter in base_sizes and last_letter != 'm':
#             modifiers = 0
#             for rest in size[:-1]:
#                 if rest == 'x':
#                     modifiers += 2
#                 else:
#                     return None
#             if last_letter == 'l':
#                 return base_sizes[last_letter] + modifiers
#             else:
#                 return base_sizes[last_letter] - modifiers
#
#
# print(size_to_number('mx'))
# print(size_to_number('xsx'))
# print(size_to_number('xxs'))
# print(size_to_number('xxl'))
# print(size_to_number('s'))
#__________________________________

def size_to_number(size):
    base_sizes = {'s': 36, 'm': 38, 'l': 40}
    current_letter = 0
    modifiers = 0
    last_letter = size[-1]
    if len(size) == 1:
        return base_sizes.get(size[current_letter], None)
    elif len(size) > 1 and last_letter in base_sizes and last_letter != 'm':
        for rest in size[:-1]:
            if rest == 'x':
                modifiers += 2
            else:
                return None
        if last_letter == 'l':
            return base_sizes[last_letter] + modifiers
        else:
            return base_sizes[last_letter] - modifiers


print(size_to_number('mx'))
print(size_to_number('xsx'))
print(size_to_number('xxs'))
print(size_to_number('xxl'))
print(size_to_number('s'))