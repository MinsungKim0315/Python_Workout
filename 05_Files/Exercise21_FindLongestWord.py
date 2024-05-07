'''
find the longest word in a text file
'''
def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word

print(find_longest_word('test.txt'))
