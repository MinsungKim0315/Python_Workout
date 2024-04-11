import operator

PEOPLE = [{
    'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'
}, {
    'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'
}, {
    'first': 'Vladmir', 'last': 'Putin', 'email': 'reuven@kremvax.ru'
}]

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key = operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))


'''
result
[{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'}, 
{'first': 'Vladmir', 'last': 'Putin', 'email': 'reuven@kremvax.ru'}, 
{'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'}]
'''