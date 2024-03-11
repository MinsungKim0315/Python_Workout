# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:52:18 2024

@author: minsung.kim
Addtitional indexing and slicing practice
"""

def even_odd_sums(sequence):
    sum_even = 0
    sum_odd = 0
    output=[0]
    for num in sequence:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    output = [sum_even, sum_odd]
    return output, type(output)

def plus_minus(sequence):
    sum_plus = 0
    sum_minus = 0
    for num in sequence[1:len(sequence):2]:
        sum_plus += num
    for num in sequence[2:len(sequence):2]:
        sum_minus += num
    return sequence[0] + sum_plus - sum_minus

print(even_odd_sums((1, 2, 3, 4, 5, 6, 7)))
print(plus_minus((10, 20, 30, 40, 50, 60)))

#zip function
a = ("a", "b", "c")
b = (1, 2, 3)
c = ['A', 'B', 'C']
result = zip(a, b, c)
print(list(result))
