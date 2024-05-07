'''
counting words, lines, characters, etc in a text
Save them in a dictionary
'''
def wordcount(filename):
    counts = {'character': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    for one_line in open(filename):
        counts['lines'] += 1
        counts['character'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())
    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')

wordcount('test.txt')
