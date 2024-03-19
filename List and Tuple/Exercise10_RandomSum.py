# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 2024

@author: minsung.kim
Sum any type
ex) mysum('abc', 'def') --> 'abcdef, mysum([1, 2, 3], [4, 5, 6]) --> [1, 2, 3, 4, 5, 6]
"""
# def mysum(*numbers):    #splat operator: allow a function to receive any number of arguments.
#     output = 0
#     for number in numbers:
#         output += number
#     return output

# print(mysum(10, 20, 30, 40, 50))

def mysum(*items):
    if not items:
        return items
    output = items[0]
    for items in items[1::]:
        output += items
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80, 90]))