# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:22:10 2024

@author: minsung.kim
Making a triangular out of name
"""

def name_triangular():
    letter_sum = ''
    name = input("Enter your name: ")
    for iterate, letter in enumerate(name):
        letter_sum += str(letter)
        print(f'{letter_sum}')

name_triangular()