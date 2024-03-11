# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:02:47 2024

@author: minsung.kim
Sort str in Unicode order
"""

def strsort():
    word = input("type is a word to sort: ")
    sort = ''.join(sorted(word))
    print(f'sorted word in Unicord order is --> {sort}')
    
strsort()
    
def sentencesort():
    sentence = input("type in a sentence to sort: ")
    # in order to disclude spaces, replace " " to "" using replace(,)
    temp = list(sentence.replace(" ", ""))
    sort = sorted(temp)
    output = ','.join(sort)
    print(f'sorted sentence in Unicord order is --> {output}')

sentencesort()