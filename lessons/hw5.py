#import math

#Task1
# l = [6, 9, 1, 0, 4, 111]
# def the_largest(l):
#     return max(l)
# print('The largest number is: ', the_largest(l))


#Task2
# input_length_side = int(input('Enter length of rectangle side, please: '))
# input_width_side = int(input('Enter width of rectangle side, please: '))
#
# def area_of_rectangle(l=input_length_side, w=input_width_side):
#     return l * w
# print('The area of rectangle is: ', area_of_rectangle())
#
#
# def area_of_triangle(l=int(input('Enter length of triangle side, please: ')), h=int(input('Enter height of triangle, please: '))):
#     return 1 / 2 * (l * h)
# print('The area of triangle is: ', area_of_triangle())
#
#
# input_radius = int(input('Enter radius of circle, please: '))
# def area_of_circle(r=input_radius):  # S = π r2
#     return round(math.pi * (r ** 2), 1)
# print('The area of circle is: ', area_of_circle())

#Task3
input_word = input('Print the word, please: ')
def check_letters(l=input_word):
    d = {}
    for i in set(l):
       d[i] = l.count(i)
    return d
print('Count of letters in the word: ', check_letters())
