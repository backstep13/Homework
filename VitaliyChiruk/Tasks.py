'''Task 4.1
Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa.'''

def replace_symbols(string):
    new = ""
    for i in string:
        if i == "\"":
            new += "\'"
        elif i == "\'":
            new += "\""
        else:
            new += i
    return print(new)

#replace_symbols('Hi "sir", my name is \'Sir\'')

'''Task 4.2
Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).'''

def is_pal(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

#print(is_pal("Kayak"))

'''Task 4.3
Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse).'''

def my_split(string, sep = None, maxsplit = -1):
    result_list = []
    if sep is None:
        sep = " "
    else:
        sep
    word = ""
    for i in string:
        if i in sep and maxsplit != 0:
            if sep != " " or word != "":
                result_list.append(word)
                word = ""
                if maxsplit > 0:
                    maxsplit -= 1
        else:
            word += i
    if sep != " " or word != "":
        result_list.append(word)
    return print(result_list)

#sentence = "One fly flies, two flies fly"
#my_split(sentence, sep="f", maxsplit=3)
#print(sentence.split(sep="f", maxsplit=3))

'''Task 4.4
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```'''

def split_by_index(s, indexes):
    result_list = []
    word = ""
    for count, value in enumerate(s):
        if count in indexes:
            result_list.append(word)
            word = value
        else:
            word += value
    result_list.append(word)
    return print(result_list)

#split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])

'''Task 4.5
Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
>>> split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```'''

def get_digits(num):
    result = tuple(map(int, str(num)))
    return print(result)

#get_digits(11565478)

'''Task 4.6
Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first.
Example:
```python

>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
```'''

def get_shortest_word(s):
    current_word = ""
    current_longest = ""
    for i in s:
        if i == " ":
            if len(current_word) > len(current_longest):
                current_longest = current_word
                current_word = ""
        else:
            current_word += i

    if len(current_word) > len(current_longest):
        current_longest = current_word
    return print(current_longest)

#get_shortest_word("Any pythonista like namespaces a lot")

'''Task 4.7
Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
```'''

def foo(List):
    from functools import reduce
    m = reduce(lambda x, y: x * y, List)
    return print(list(map(lambda x: m // x, List)))

#foo([1, 2, 3, 4, 5])

'''Task 4.8
Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead.
Example:
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
```'''

def get_pairs(lst):
    return print(list(zip(lst[:-1], lst[1:])))

#get_pairs([1, 2, 3, 8, 9])

'''Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string
Note: use `string.ascii_lowercase` for list of alphabet letters
```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```'''

import string

def test_1_1(*args):
    result_set = set(args[0])
    for i in args[1:]:
        result_set = result_set.intersection(i)
    return result_set

def test_1_2(*args):
    result_set = set(args[0])
    for i in args[1:]:
        result_set = result_set.union(i)
    return result_set

def test_1_3(*args):
    result_set = set()
    first = set(args[0])
    for i in args[1:]:
        result_set.update(first.intersection(i))
    return result_set

def test_1_4(*args):
    result_set = set(string.ascii_lowercase)
    for i in args:
        result_set = result_set.difference(i)
    return result_set

test_strings = ["hello", "world", "python", ]
#print(test_1_1(*test_strings))
#>>> {'o'}
#print(test_1_2(*test_strings))
#>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
#print(test_1_3(*test_strings))
#>>> {'h', 'l', 'o'}
#print(test_1_4(*test_strings))
#>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}

'''Task 4.10
Implement a function that takes a number as an argument and returns a dictionary, 
where the key is a number and the value is the square of that number.
```python
print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''

def generate_squares(number):
    return print({i: i**2 for i in range(1, number + 1)})

#generate_squares(9)

'''Task 4.11
Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
Dict values ​​should be summarized in case of identical keys
```python
def combine_dicts(*args):
    ...
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
>>> {'a': 300, 'b': 200, 'c': 300}
print(combine_dicts(dict_1, dict_2, dict_3)
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
```'''

def combine_dicts(*args):
    result_dict = {}
    for i in args:
        for key_dict, value_dict in i.items():
            result_dict[key_dict] = result_dict.get(key_dict, 0) + value_dict
    return result_dict

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
#print(combine_dicts(dict_1, dict_2))
#print(combine_dicts(dict_1, dict_2, dict_3))