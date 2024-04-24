# Python
## Python notes
* 의미 없는 소수점 제거
```python
output_a = 52.0
output_b = "{:g}".format(output_a)
```
* 대소문자 바꾸기: upper(), lower()
```python
a = "Hello Python Programming"
print(a.upper())
>> HELLO PYTHON PROGRAMMING
print(a.lower())
>> hello python programming
```
* 문자열 양옆의 공백 제거: strip()
```python
intput_a = '''
    안녕하세요
문자열의 함수를 알아봅시다
'''
print(input_a.strip())
>> 안녕하세요
    문자열의 함수를 알아봅시다
```
* 문자열의 구성 파악: isOO()
>   + isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는 확인
>   + isalpha(): 문자열이 알파벳으로만 구성되어 있는 확인
>   + isidentifier(): 문자열이 식별자로 사용되는지 확인
>   + isdecimal(): 문자열이 정수 형태인지 확인
>   + isdigit(): 문자열이 숫자로 인식될 수 있는 확인
>   + isspace(): 문자열이 공백으로만
>   + islower(): 문자열이 소문자로만
>   + isupper(): 문자열이 대문자로만
* 문자열 찾기: find(), rfind()
>   * 없으면 -1 출력
```python
a = "hello".find("e")
b = "hello".rfind("e")
print(a)
>> 1
print(b)
>> 3
```
* 문자열과 in: 문자열 내부에 어떤 문자열이 있는지 확인
```python
text = "Hello, world!"

if "world" in text:
    print("부분 문자열이 존재합니다.")
else:
    print("부분 문자열이 존재하지 않습니다.")

```
* 문자열 자르기: split()
>   1. 기본 사용법: 문자열을 공백 기준으로 분리
```python
sentence = "Hello world"
words = sentence.split()
print(words)  # ['Hello', 'world']
```
>   2. 구분자 지정: 구분자를 인자로 전달하여 문자열을 해당 구분자 기준으로 분리
```python
sentence = "apple,banana,grape"
fruits = sentence.split(",")
print(fruits)  # ['apple', 'banana', 'grape']
```
>   3. 분리할 개수 제한: 두 번째 인자로 분리할 최대 개수 지정
```python
sentence = "apple banana grape orange"
words = sentence.split(" ", 2)
print(words)  # ['apple', 'banana', 'grape orange']
```
>   4. 공백 제거: 기본적으로 분리된 문자열 사이에 있는 공백은 제거
* 리스트에 요소 추가: append, insert
>   1. append(): 리스트의 끝에 요소를 추가
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # 출력: [1, 2, 3, 4]
```
>   2. insert():  리스트의 특정 위치에 요소를 삽입
```python
numbers = [1, 2, 3, 4]
numbers.insert(2, 2.5)
print(numbers)  # 출력: [1, 2, 2.5, 3, 4]
```
>   3. extend():  리스트에 다른 리스트의 모든 요소를 추가
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # 출력: [1, 2, 3, 4, 5, 6]

```
* 리스트에 요소 제거: del, pop(), remove(), clear()
>   1. del: 리스트에서 지정된 인덱스에 있는 요소나 슬라이스를 제거
```python
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print(numbers)  # 출력: [2, 3, 4, 5]

del numbers[1:3]
print(numbers)  # 출력: [2, 5]
```
>   2. pop(): 리스트에서 지정된 인덱스에 있는 요소를 제거하고 반환합니다. 
인덱스를 지정하지 않으면 리스트의 마지막 요소가 제거
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
print(numbers)  # 출력: [1, 2, 4, 5]
```
>   3. remove(): 리스트에서 지정된 값과 일치하는 첫 번째 요소를 제거
```python
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)  # 출력: [1, 2, 4, 5]
```
>   4. clear(): 리스트의 모든 요소를 제거
```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # 출력: []
```
* 멤버십 연산자: in/ not in
>   1. in
```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # 출력: True
```
>   2. not in
```python
my_list = [1, 2, 3, 4, 5]
print(6 not in my_list)  # 출력: True
```
* 딕셔너리에 값 추가하기/제거하기
>   1. 값 추가하기: 키 지정하고 새로운 값 할당
```python
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # 새로운 키 'c'에 값 3 추가
print(my_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3}
```
>   2. 값 제거하기: del, pop(), popitem(), clear()
```python
# 특정 키-값 쌍을 제거하려면 del 키워드를 사용하여 해당 키를 제거
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  # 키 'b'에 해당하는 값 제거
print(my_dict)  # 출력: {'a': 1, 'c': 3}
```
```python
# pop() 메서드를 사용하여 특정 키에 해당하는 값을 제거
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_value = my_dict.pop('b')  # 키 'b'에 해당하는 값 제거 및 반환
print(my_dict)  # 출력: {'a': 1, 'c': 3}
print(removed_value)  # 출력: 2
```
```python
# popitem() 메서드를 사용하여 딕셔너리에서 마지막 키-값 쌍을 제거
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_item = my_dict.popitem()  # 마지막 키-값 쌍 제거 및 반환
print(my_dict)  # 출력: {'a': 1, 'b': 2}
print(removed_item)  # 출력: ('c', 3)
```
```python
# clear() 메서드를 사용하여 딕셔너리의 모든 요소를 제거
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()  # 모든 요소 제거
print(my_dict)  # 출력: {}
```
* 딕셔너리 내부에 키가 있는지 확인
>   1. in: 딕셔너리에서 특정 키가 존재하는지 여부를 확인
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)  # 출력: True
print('d' in my_dict)  # 출력: False
```
>   2. get(): 딕셔너리에서 특정 키에 해당하는 값을 가져옵니다. 키가 존재하지 않는 경우 기본값을 반환
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # 출력: 1
print(my_dict.get('d'))  # 출력: None
```
* for 반복문 반대로 반복하기
>   1. range() 함수의 매개변수를 세 개 사용
```python
for i in range(4, -1, -1):
    print(i)    # 출력: 4, 3, 2, 1, 0
```
>   2. reversed()
```python
for i reversed(range(5)):
    print(i)    # 출력: 4, 3, 2, 1, 0
```
*문자열, 리스트, 딕셔너리와 관련된 함수
>   1. min(), max(), sum()
```python
my_list = [5, 2, 8, 1, 9]
print(min(my_list))  # 출력: 1
print(max(my_list))  # 출력: 9
print(sum(my_list))  # 출력: 25
```
>   2. reversed()
```python
my_list = [1, 2, 3, 4, 5]

for item in reversed(my_list):
    print(item)
```
>   3. enumerate(): iterable 객체를 받아 인덱스와 해당요소를 반환
```python
my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list):
    print(index, value)
# 0 apple
# 1 banana
# 2 orange
```
>   4. items(): 딕셔너리의 각 키-값 쌍을 반환
```python
my_dict = {'apple': 2, 'banana': 3, 'orange': 5}

for key, value in my_dict.items():
    print(key, value)
# apple 2
# banana 3
# orange 5
```
>   5. 리스트 내포: 반복문을 사용하여 리스트를 만드는 방법을 단축시킨 구문
```python
# 형태: [표현식 for 요소 in iterable if 조건(선택 사항)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) #[0, 4, 16, 36, 64]

array = [i * i in range(0, 10, 2)]
print(array)    #[0, 4, 16, 36, 64, 100]
```
* 가변 매개변수: 함수에 임의의 개수의 인자를 전달할 수 있게 해주는 매커니즘
>   * 가변 매개변수 뒤에는 일반 매개변수 올 수 없다
>   * 가변 매개변수는 하나만 사용가능
>   1. *args: 임의의 개수의 위치 인자를 받음, 인자들은 튜플 형태로 함수 내에서 접근
```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
# 1
# 2
# 3
```
>   2. **kwargs: 임의의 개수의 키워드 인자를 받음, 인자들은 딕셔너리 형태로 함수 내에서 접근
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(a=1, b=2, c=3)
# a: 1
# b: 2
# c: 3
```
* 순서가 있는(iterable) 객체를 정렬한 새로운 리스트를 반환: sorted()
```python
#기본 형태
sorted(iterable, key = None, reverse = False)

#리스트 정렬
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(my_list)
print(sorted_list)  # 출력: [1, 1, 2, 3, 4, 5, 6, 9]

#문자열 정렬
my_string = "python"
sorted_string = sorted(my_string)
print(sorted_string)  # 출력: ['h', 'n', 'o', 'p', 't', 'y']

#요소의 특정 속성이나 함수를 기준으로 정렬
my_list = [('apple', 3), ('banana', 2), ('orange', 5), ('grape', 1)]

# 두 번째 요소를 기준으로 정렬
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)
# 출력: [('grape', 1), ('banana', 2), ('apple', 3), ('orange', 5)]
```
>   * operator.itemgetter 이용하면 lambda 함수 사용을 대신하여 더 간결하고 효율적으로 특정 인덱스의 요소를 가져올 수 있음
```python
import operator

my_list = [('apple', 3), ('banana', 2), ('orange', 5), ('grape', 1)]

# 두 번째 요소를 기준으로 정렬
sorted_list = sorted(my_list, key=operator.itemgetter(1))
print(sorted_list)
# 출력: [('grape', 1), ('banana', 2), ('apple', 3), ('orange', 5)]
```
>   * custom key: 요소를 정렬할 때 기준을 제공하기 위해 사용자가 정의한 함수
```python
my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']

# Define a custom key function to return the length of a string
def get_length(word):
    return len(word)

# Sort the list based on the length of each string
sorted_list = sorted(my_list, key=get_length)
print(sorted_list)
# 출력: ['kiwi', 'pear', 'apple', 'grape', 'banana', 'orange']
```
* collections 모듈의 Counter class: 반복 가능한(iterable) 객체의 요소를 세는 데 사용
```python
from collections import Counter

# 문자열에서 각 문자의 출현 빈도를 세기
s = 'apple'
count = Counter(s)
print(count)
# 출력: Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
```
>   * most_common() 메서드: 가장 많이 출현한 요소들을 순서대로 반환
```python
from collections import Counter

s = 'abracadabra'
count = Counter(s)

# 가장 많이 출현한 요소들을 순서대로 출력
print(count.most_common())
# 출력: [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```
*  iterable(반복 가능한 객체)에서 가장 큰 요소를 반환: max()
```python
numbers = [1, 3, 5, 7, 9]
max_number = max(numbers)
print(max_number)  # 출력: 9

strings = ['apple', 'banana', 'orange']
max_string = max(strings)
print(max_string)  # 출력: 'orange'

```
>   * key 매개변수 허용
```python
strings = ['apple', 'banana', 'orange']
max_string = max(strings, key=len)  # 문자열의 길이를 기준으로 최댓값을 찾음
print(max_string)  # 출력: 'banana'

def last_character(s):
    return s[-1]

max_string = max(strings, key=last_character)  # 각 문자열의 마지막 문자를 기준으로 최댓값을 찾음
print(max_string)  # 출력: 'banana'
```
* 전개 연산자(*): 여러 요소가 있는 iterable를 사용하여 함수 호출이나 컬렉션(lsit, tuple 등)을 생성할 때 요소를 풀어서 사용하는 역할
>   1. 함수 호출: 함수 호출 시 인수로 iterable을 전달할 때
```python
def add(x, y, z):
    return x + y + z

numbers = [1, 2, 3]
result = add(*numbers)  # numbers 리스트의 요소를 add 함수의 인수로 전달
print(result)  # 출력: 6
```
>   2. 컬렉션 생성에서의 사용: 컬렉션을 만들 때 다른 컬렉션의 요소를 풀어서 사용할 때
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]  # 두 리스트를 하나로 합침
print(merged_list)  # 출력: [1, 2, 3, 4, 5, 6]
```
* Dictionary 사용법
>   1. 작은 데이터베이스 또는 레코드로 사용
>   2. 변수를 여러 개 선언할 필요없이, 딕셔너리를 하나 선언하고, 딕셔너리에 여러 개의 키-값 쌍을 넣어서 사용
>   3. 시간에 따라 변화하는 정보를 누적해서 기록할 때 사용
>   * 키 부분: 해시 함수를 적용해서 해시를 만들어낼 수 있는 것만 사용, 뮤터블 객체를 키로 사용할 수 없음
* set: 값이 없는 딕셔너리
>   1. 거대한 컬렉션에서 무언가를 탐색할 때
>   2. 목록에서 중복을 제거할 때
* 딕셔너리 관현 메서드
>   1. dict.keys(): 딕셔너리의 키(key)들을 반환
>   2. dict.values():딕셔너리의 값(value)들을 반환
>   3. dict.items(): 딕셔너리의 키-값 쌍(key-value pair)들을 반환
>   4. dict.get(key, default): 주어진 키에 대응하는 값을 반환합니다. 키가 없을 경우 기본값(default)을 반환
* set(): 주어진 시퀀스나 다른 이터러블 객체를 사용하여 새로운 세트를 생성. 이때 생성된 세트는 중복을 허용하지 않고 순서가 없는 데이터 집합
```python
my_list = [1, 2, 3, 3, 4, 5, 5]
my_set = set(my_list)
print(my_set)  # 출력: {1, 2, 3, 4, 5}
```
* Memoization
>   1. 딕셔너리를 사용해서 한 번 계산한 값을 저장함. 이렇게 메모가 되어 있으면 처리를 수행하지 않고 곧바로 메모된 값을 돌려주면서 코드의 속도를 빠르게 만듬
>   2. 재귀함수와 함께 많이 사용되는 기술
```python
dictionary = {
    1: 1,
    2: 1
}
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        ouput = new_fib(n-1) + new_fib(n-2)
        dictionary[n] = ouput
        return ouput
```
* 함수를 매개변수로 전달하는 중요 표준 함수
>   1. map(function, iterable, *iterables):  
>   해당 함수를 반복 가능한 객체의 각 요소에 적용하고, 그 결과를   새로운 리스트로 반환
>   2. filter(fuction, iterable):  
> 해당 함수를 반복 가능한 객체의 각 요소에 적용하고, 함수가 True를 반환하는 요소만 선택하여 새로운 리스트로 반환
> > * lamda arguments: expression  
> > ->  anonymous function that can have any number of arguments but can only have one expression  
> > -> used when you're passing a function as an argument to another function or when you want to create a quick inline function
```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x:x**2, numbers)
even_nums = filter(lambda x: x % 2 == 0, numbers)
print(list(squared))    #result: [1, 4, 9, 16, 25]
print(list(even_nums))  #result: [2, 4]
```
* 파일 처리
>   1. 형태: 파일 객체 = open("파일 경로", "모드")
>   2. 모드:  
> w -> write; 새로 쓰기 모드  
> a -> append; 뒤에서 이어서 쓰기  
> r -> read; 읽기
> > *  파일 닫기: 파일 객체.close()
> > * with 키워드: with 구문이 종료될 때 자동으로 파일 닫힘  
> > ```python
> >with open('example.txt', 'w') as file:
> >     file.write('hello world')
> >     contents = file.read()
> >print(contents)  #result: hello world
> >```
> > * 텍스트를 사용해 데이터를 구조적으로 표현: CSV, XML, JSON
> > > * CSV: 한 줄에 하나의 데이터를 나타내며, 각각의 줄은 쉼표를 사용해 데이터 구분
```python
import random

alphabet = list('abcdefghijklmnop')
with open('test.txt', 'w')as file:
    for i in range(1000):
        name = random.choice(alphabet) + random.choice(alphabet)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        # write data in text file in CSV format
        file.write(f'{name}, {weight}, {height}\n')

with open('test.txt', 'r') as file:
    # read data line by line
    for line in file:
        # define variables
        (name, weight, height) = line.strip().split(', ')

        if(not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) **2)
        result = ''
        if 25 <= bmi:
            result = 'over weight'
        elif 18.5 <= bmi:
            result = 'normal'
        else:
            result = 'low'
        
        print(f'name: {name}\n'
            f'weight: {weight}\n'
            f'height: {height}\n'
            f'BMI: {bmi}\n'
            f'result: {result}')
```
* all(iterable): Return True if all elements of the iterable are true
```python
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        num_str = str(num)
        if all(char in '05' for char in num_str):
            answer.append(num)

    return answer if answer else [-1]
print(solution(5, 555)) #result: [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20)) #result: [-1]
```
## Python codes
* 플래그 이용, 배열 안의 아이템 접근법
```python
def solution(arr, queries):
    answer = []
    for query in queries:
        i, j, k = query
        sub_arr = arr[i:j+1]
        sub_arr.sort()
        found = False
        for num in sub_arr:
            if num > k:
                answer.append(num)
                found = True
                break
        if not found:
            answer.append(-1)
    
    return answer
print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))   #result: [3, 4, -1]
```
* 쿼리 배열 안의 item들을 조건으로 사용할 때 item들에 이름 지정
```python
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다. 위 규칙에 따라 queries를 처리한 이후의 arr를 return
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1], [0, 3, 2], [0, 3, 3]]
temp = []
for query in queries:
    start, end, divisor = query
    for i in range(start, end + 1):
        if i % divisor == 0:
            temp.append(i)
for i in range(len(arr)):
    for num in temp:
        if i == num:
            arr[i] += 1

print(arr)  #result: [3, 2, 4, 6, 4]
```
