# Python note
* �ǹ� ���� �Ҽ��� ����
```python
output_a = 52.0
output_b = "{:g}".format(output_a)
```
* ��ҹ��� �ٲٱ�: upper(), lower()
```python
a = "Hello Python Programming"
print(a.upper())
>> HELLO PYTHON PROGRAMMING
print(a.lower())
>> hello python programming
```
* ���ڿ� �翷�� ���� ����: strip()
```python
intput_a = '''
    �ȳ��ϼ���
���ڿ��� �Լ��� �˾ƺ��ô�
'''
print(input_a.strip())
>> �ȳ��ϼ���
    ���ڿ��� �Լ��� �˾ƺ��ô�
```
* ���ڿ��� ���� �ľ�: isOO()
>   + isalnum(): ���ڿ��� ���ĺ� �Ǵ� ���ڷθ� �����Ǿ� �ִ� Ȯ��
>   + isalpha(): ���ڿ��� ���ĺ����θ� �����Ǿ� �ִ� Ȯ��
>   + isidentifier(): ���ڿ��� �ĺ��ڷ� ���Ǵ��� Ȯ��
>   + isdecimal(): ���ڿ��� ���� �������� Ȯ��
>   + isdigit(): ���ڿ��� ���ڷ� �νĵ� �� �ִ� Ȯ��
>   + isspace(): ���ڿ��� �������θ�
>   + islower(): ���ڿ��� �ҹ��ڷθ�
>   + isupper(): ���ڿ��� �빮�ڷθ�
* ���ڿ� ã��: find(), rfind()
>   * ������ -1 ���
```python
a = "hello".find("e")
b = "hello".rfind("e")
print(a)
>> 1
print(b)
>> 3
```
* ���ڿ��� in: ���ڿ� ���ο� � ���ڿ��� �ִ��� Ȯ��
```python
text = "Hello, world!"

if "world" in text:
    print("�κ� ���ڿ��� �����մϴ�.")
else:
    print("�κ� ���ڿ��� �������� �ʽ��ϴ�.")

```
* ���ڿ� �ڸ���: split()
>   1. �⺻ ����: ���ڿ��� ���� �������� �и�
```python
sentence = "Hello world"
words = sentence.split()
print(words)  # ['Hello', 'world']
```
>   2. ������ ����: �����ڸ� ���ڷ� �����Ͽ� ���ڿ��� �ش� ������ �������� �и�
```python
sentence = "apple,banana,grape"
fruits = sentence.split(",")
print(fruits)  # ['apple', 'banana', 'grape']
```
>   3. �и��� ���� ����: �� ��° ���ڷ� �и��� �ִ� ���� ����
```python
sentence = "apple banana grape orange"
words = sentence.split(" ", 2)
print(words)  # ['apple', 'banana', 'grape orange']
```
>   4. ���� ����: �⺻������ �и��� ���ڿ� ���̿� �ִ� ������ ����
* ����Ʈ�� ��� �߰�: append, insert
>   1. append(): ����Ʈ�� ���� ��Ҹ� �߰�
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # ���: [1, 2, 3, 4]
```
>   2. insert():  ����Ʈ�� Ư�� ��ġ�� ��Ҹ� ����
```python
numbers = [1, 2, 3, 4]
numbers.insert(2, 2.5)
print(numbers)  # ���: [1, 2, 2.5, 3, 4]
```
>   3. extend():  ����Ʈ�� �ٸ� ����Ʈ�� ��� ��Ҹ� �߰�
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # ���: [1, 2, 3, 4, 5, 6]

```
* ����Ʈ�� ��� ����: del, pop(), remove(), clear()
>   1. del: ����Ʈ���� ������ �ε����� �ִ� ��ҳ� �����̽��� ����
```python
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print(numbers)  # ���: [2, 3, 4, 5]

del numbers[1:3]
print(numbers)  # ���: [2, 5]
```
>   2. pop(): ����Ʈ���� ������ �ε����� �ִ� ��Ҹ� �����ϰ� ��ȯ�մϴ�. 
�ε����� �������� ������ ����Ʈ�� ������ ��Ұ� ����
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
print(numbers)  # ���: [1, 2, 4, 5]
```
>   3. remove(): ����Ʈ���� ������ ���� ��ġ�ϴ� ù ��° ��Ҹ� ����
```python
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)  # ���: [1, 2, 4, 5]
```
>   4. clear(): ����Ʈ�� ��� ��Ҹ� ����
```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # ���: []
```
* ����� ������: in/ not in
>   1. in
```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # ���: True
```
>   2. not in
```python
my_list = [1, 2, 3, 4, 5]
print(6 not in my_list)  # ���: True
```
* ��ųʸ��� �� �߰��ϱ�/�����ϱ�
>   1. �� �߰��ϱ�: Ű �����ϰ� ���ο� �� �Ҵ�
```python
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # ���ο� Ű 'c'�� �� 3 �߰�
print(my_dict)  # ���: {'a': 1, 'b': 2, 'c': 3}
```
>   2. �� �����ϱ�: del, pop(), popitem(), clear()
```python
# Ư�� Ű-�� ���� �����Ϸ��� del Ű���带 ����Ͽ� �ش� Ű�� ����
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  # Ű 'b'�� �ش��ϴ� �� ����
print(my_dict)  # ���: {'a': 1, 'c': 3}
```
```python
# pop() �޼��带 ����Ͽ� Ư�� Ű�� �ش��ϴ� ���� ����
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_value = my_dict.pop('b')  # Ű 'b'�� �ش��ϴ� �� ���� �� ��ȯ
print(my_dict)  # ���: {'a': 1, 'c': 3}
print(removed_value)  # ���: 2
```
```python
# popitem() �޼��带 ����Ͽ� ��ųʸ����� ������ Ű-�� ���� ����
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_item = my_dict.popitem()  # ������ Ű-�� �� ���� �� ��ȯ
print(my_dict)  # ���: {'a': 1, 'b': 2}
print(removed_item)  # ���: ('c', 3)
```
```python
# clear() �޼��带 ����Ͽ� ��ųʸ��� ��� ��Ҹ� ����
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()  # ��� ��� ����
print(my_dict)  # ���: {}
```
* ��ųʸ� ���ο� Ű�� �ִ��� Ȯ��
>   1. in: ��ųʸ����� Ư�� Ű�� �����ϴ��� ���θ� Ȯ��
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)  # ���: True
print('d' in my_dict)  # ���: False
```
>   2. get(): ��ųʸ����� Ư�� Ű�� �ش��ϴ� ���� �����ɴϴ�. Ű�� �������� �ʴ� ��� �⺻���� ��ȯ
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # ���: 1
print(my_dict.get('d'))  # ���: None
```
* for �ݺ��� �ݴ�� �ݺ��ϱ�
>   1. range() �Լ��� �Ű������� �� �� ���
```python
for i in range(4, -1, -1):
    print(i)    # ���: 4, 3, 2, 1, 0
```
>   2. reversed()
```python
for i reversed(range(5)):
    print(i)    # ���: 4, 3, 2, 1, 0
```
*���ڿ�, ����Ʈ, ��ųʸ��� ���õ� �Լ�
>   1. min(), max(), sum()
```python
my_list = [5, 2, 8, 1, 9]
print(min(my_list))  # ���: 1
print(max(my_list))  # ���: 9
print(sum(my_list))  # ���: 25
```
>   2. reversed()
```python
my_list = [1, 2, 3, 4, 5]

for item in reversed(my_list):
    print(item)
```
>   3. enumerate(): iterable ��ü�� �޾� �ε����� �ش��Ҹ� ��ȯ
```python
my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list):
    print(index, value)
# 0 apple
# 1 banana
# 2 orange
```
>   4. items(): ��ųʸ��� �� Ű-�� ���� ��ȯ
```python
my_dict = {'apple': 2, 'banana': 3, 'orange': 5}

for key, value in my_dict.items():
    print(key, value)
# apple 2
# banana 3
# orange 5
```
>   5. ����Ʈ ����: �ݺ����� ����Ͽ� ����Ʈ�� ����� ����� �����Ų ����
```python
# ����: [ǥ���� for ��� in iterable if ����(���� ����)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) #[0, 4, 16, 36, 64]

array = [i * i in range(0, 10, 2)]
print(array)    #[0, 4, 16, 36, 64, 100]
```
* ���� �Ű�����: �Լ��� ������ ������ ���ڸ� ������ �� �ְ� ���ִ� ��Ŀ����
>   * ���� �Ű����� �ڿ��� �Ϲ� �Ű����� �� �� ����
>   * ���� �Ű������� �ϳ��� ��밡��
>   1. *args: ������ ������ ��ġ ���ڸ� ����, ���ڵ��� Ʃ�� ���·� �Լ� ������ ����
```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
# 1
# 2
# 3
```
>   2. **kwargs: ������ ������ Ű���� ���ڸ� ����, ���ڵ��� ��ųʸ� ���·� �Լ� ������ ����
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(a=1, b=2, c=3)
# a: 1
# b: 2
# c: 3
```
* ������ �ִ�(iterable) ��ü�� ������ ���ο� ����Ʈ�� ��ȯ: sorted()
```python
#�⺻ ����
sorted(iterable, key = None, reverse = False)

#����Ʈ ����
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(my_list)
print(sorted_list)  # ���: [1, 1, 2, 3, 4, 5, 6, 9]

#���ڿ� ����
my_string = "python"
sorted_string = sorted(my_string)
print(sorted_string)  # ���: ['h', 'n', 'o', 'p', 't', 'y']

#����� Ư�� �Ӽ��̳� �Լ��� �������� ����
my_list = [('apple', 3), ('banana', 2), ('orange', 5), ('grape', 1)]

# �� ��° ��Ҹ� �������� ����
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)
# ���: [('grape', 1), ('banana', 2), ('apple', 3), ('orange', 5)]
```
>   * operator.itemgetter �̿��ϸ� lambda �Լ� ����� ����Ͽ� �� �����ϰ� ȿ�������� Ư�� �ε����� ��Ҹ� ������ �� ����
```python
import operator

my_list = [('apple', 3), ('banana', 2), ('orange', 5), ('grape', 1)]

# �� ��° ��Ҹ� �������� ����
sorted_list = sorted(my_list, key=operator.itemgetter(1))
print(sorted_list)
# ���: [('grape', 1), ('banana', 2), ('apple', 3), ('orange', 5)]
```
>   * custom key: ��Ҹ� ������ �� ������ �����ϱ� ���� ����ڰ� ������ �Լ�
```python
my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']

# Define a custom key function to return the length of a string
def get_length(word):
    return len(word)

# Sort the list based on the length of each string
sorted_list = sorted(my_list, key=get_length)
print(sorted_list)
# ���: ['kiwi', 'pear', 'apple', 'grape', 'banana', 'orange']
```
* collections ����� Counter class: �ݺ� ������(iterable) ��ü�� ��Ҹ� ���� �� ���
```python
from collections import Counter

# ���ڿ����� �� ������ ���� �󵵸� ����
s = 'apple'
count = Counter(s)
print(count)
# ���: Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
```
>   * most_common() �޼���: ���� ���� ������ ��ҵ��� ������� ��ȯ
```python
from collections import Counter

s = 'abracadabra'
count = Counter(s)

# ���� ���� ������ ��ҵ��� ������� ���
print(count.most_common())
# ���: [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```
*  iterable(�ݺ� ������ ��ü)���� ���� ū ��Ҹ� ��ȯ: max()
```python
numbers = [1, 3, 5, 7, 9]
max_number = max(numbers)
print(max_number)  # ���: 9

strings = ['apple', 'banana', 'orange']
max_string = max(strings)
print(max_string)  # ���: 'orange'

```
>   * key �Ű����� ���
```python
strings = ['apple', 'banana', 'orange']
max_string = max(strings, key=len)  # ���ڿ��� ���̸� �������� �ִ��� ã��
print(max_string)  # ���: 'banana'

def last_character(s):
    return s[-1]

max_string = max(strings, key=last_character)  # �� ���ڿ��� ������ ���ڸ� �������� �ִ��� ã��
print(max_string)  # ���: 'banana'
```
* ���� ������(*): ���� ��Ұ� �ִ� iterable�� ����Ͽ� �Լ� ȣ���̳� �÷���(lsit, tuple ��)�� ������ �� ��Ҹ� Ǯ� ����ϴ� ����
>   1. �Լ� ȣ��: �Լ� ȣ�� �� �μ��� iterable�� ������ ��
```python
def add(x, y, z):
    return x + y + z

numbers = [1, 2, 3]
result = add(*numbers)  # numbers ����Ʈ�� ��Ҹ� add �Լ��� �μ��� ����
print(result)  # ���: 6
```
>   2. �÷��� ���������� ���: �÷����� ���� �� �ٸ� �÷����� ��Ҹ� Ǯ� ����� ��
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]  # �� ����Ʈ�� �ϳ��� ��ħ
print(merged_list)  # ���: [1, 2, 3, 4, 5, 6]
```