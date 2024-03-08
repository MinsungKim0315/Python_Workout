# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:07:17 2024

@author: minsung.kim
Same rule with pig latin word
instead of a word, it is now a sentence
ex) this is a test translation --> histay isway away esttay ranslationtay
"""

# str.split() method
# fruits = "Appe, Bannana, Orange"
# fruit = fruits.split(',')
# print(fruit)
# sentence = "Hello world! How are you?"
# word = sentence.split()
# print(word)

def pl_sentence():
    sentence = input("Type in a sentence: ")
    output = []
    for word in sentence.split():
        if word[0] in 'aeioou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    print(' '.join(output))
        
pl_sentence()
