# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:20:39 2024

@author: minsung.kim
extract the fist and last component of a sequence, 
combine the two elements,
return it in its original type
"""

def firstlast(sequence):
   return sequence[:1] + sequence[-1:]

print(firstlast((1, 2, 3, 4, 5, 6, 7, 8, 9)))