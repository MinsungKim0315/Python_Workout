from collections import Counter
import operator

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_counter(word):
    return Counter(word).most_common(1)[0][1]
def most_repeating_word(words):
    return max(words, key=most_repeating_letter_counter)

print(most_repeating_word(WORDS))