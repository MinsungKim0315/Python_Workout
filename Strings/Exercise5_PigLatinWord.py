# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:14:11 2024

@author: minsung.kim
pig_latin rule:
    if a word starts with a vowel, put 'way' on the end of the word
    ex) air --> airway
    elif, move the first letter to the end of the word and add 'ay'
    ex) python --> ythonpway, computer --> omputercay
"""

def pig_latin():
    word = input("Type in a word: ")
    if word[0] in 'aeiouAEIOU':
        # word = word + 'way'
        word = f'{word}way'
    else:
        # word = word[1:len(word)] + word[0] + 'ay'
        word = f'{word[1].upper()}{word[2:]}{word[0].lower()}ay'
    print(word)

pig_latin()