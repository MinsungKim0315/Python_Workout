# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:21:10 2024

@author: minsung.kim
['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] -->
['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
"""

# a = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
# new1 = []
# new2 = []
# new3 = []
# output = []
# new1.append(a[0].split(' ')[0])
# new2.append(a[0].split(' ')[1])
# new3.append(a[0].split(' ')[2])
# new1.append(a[1].split(' ')[0])
# new2.append(a[1].split(' ')[1])
# new3.append(a[1].split(' ')[2])
# new1.append(a[2].split(' ')[0])
# new2.append(a[2].split(' ')[1])
# new3.append(a[2].split(' ')[2])

# output =[' '.join(new1), ' '.join(new2), ' '.join(new3)]
# print(output)

a = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

# Split each string into words and store them in separate lists
words_lists = [item.split() for item in a]
# Create the output list by joining corresponding words
output = []
for i in range(len(words_lists[0])):
    joined_words = ' '.join(words[i] for words in words_lists)
    output.append(joined_words)
    
print(output)