STRING = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']

def vowel_nums(list_of_string):

    def get_vowel(word):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
        return sum(1 for char in word if char in vowels)
    
    sorted_list = sorted(list_of_string, key=get_vowel)

    return sorted_list

print(vowel_nums(STRING))