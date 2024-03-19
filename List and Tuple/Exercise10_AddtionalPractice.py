# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 2024

@author: minsung.kim
Sum only integers and changable integers in various types
ex) sum_numeric(10, 20, 'a', '30', 'bcd') --> 60
"""
'''
isinstance(object, classinfo) function
: check if an object belongs to a particular class or data type
'''
def sum_numeric(*items):
    if not items:
        return items
    output = 0
    for items in items:
        if isinstance(items, int):
            output += items
    return output

print(sum_numeric(10, 20, 'a', '30', 'bcd'))