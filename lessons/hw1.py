# str = 'never better is'
# print(str.find('n'), str.find('e'), str.find('r'), str.find('b'), str.find('i'), str.find('s'))
# print(str.upper())
# print(str.replace('i', '&'))
import math

l = [5,6,3,8]
print(l)
print(list(reversed(l)))
print(math.prod(l))
print(sorted(l))
l[0], l[1] = l[1], l[0]
print(l)

