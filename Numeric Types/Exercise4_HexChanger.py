# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:19:27 2024

@author: minsung.kim
input 16 hex, convert it to 10 hex
use function: reversed and enumerate
"""

#enumerate function
# for i, one_letter in enumerate('1233545676ew52352'):
#     print(f"{i}: {one_letter}")

#reversed function
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in reversed(num_list):
#     print(num)
# name = "william"
# reversed_name = ''.join(reversed(name))
# print(f'reversed version is {reversed_name}')

def hex_output():
    converted_num = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        converted_num += int(digit, 16) * (16 ** power)
        print(converted_num)
    print(converted_num)
    
hex_output()
    