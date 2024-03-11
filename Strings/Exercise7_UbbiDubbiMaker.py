# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:37:00 2024

@author: minsung.kim
Ubbi Dubbi program:
    insert 'ub' in front of every 'aeiou'
ex) milk --> mubilk, soap --> suboubap
"""

def ubbi_dubbi():
    word = input("type in a word: ")
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    result = ''.join(output)
    print(f'ubbi dubbi word --> {result}')
    
ubbi_dubbi()
    