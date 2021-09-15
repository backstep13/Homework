'''Task 1.1
Write a Python program to calculate the length of a string without using the `len` function.'''
def length_of_string(string):
    a = 0
    for i in string:
        a += 1
    return print(a)

#length_of_string("ololololo")

'''Task 1.2
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters)
Input: 'Oh, it is python' 
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}'''
def count_symbol(string):
    a = dict()
    for i in string.lower():
        keys = a.keys()
        if i in keys:
            a[i] += 1
        else:
            a[i] = 1
    return print(a)

#count_symbol("hello world")

'''Task 1.3
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form.
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']'''
def sort_form(list):
    a = set(list)
    b = []
    for i in a:
        b.append(i)
    return print(sorted(b))

#sort_form(["spam", "spam", "moscow", "airbus", "zetec"])

'''Task 1.3
Create a program that asks the user for a number and then prints out a list of 
all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}'''
def divisors(a):
    b = []
    for i in range(1, a+1):
        if a % i == 0:
            b.append(i)
    return print(b)

#divisors(144)

'''Task 1.4
Write a Python program to sort a dictionary by key.'''
def sort_dict(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict)
    for i in sorted_keys:
        sorted_dict[i] = dict[i]
    return print(sorted_dict)

#sort_dict({"a":1, "e":16, "b":22, "z":2, "w":5})

'''Task 1.5
Write a Python program to print all unique values of all dictionaries in a list.
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}'''

def unique_values(list):
    a = []
    for i in list:
        for key in i:
            a.append(i[key])
    return print(set(a))

#unique_values([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])

'''Task 1.6
Write a Python program to convert a given tuple of positive integers into an integer.
Input: (1, 2, 3, 4)
Output: 1234'''
def integer_number(tuple):
    a = ""
    for i in tuple:
        a += str(i)
    return print(int(a))

#integer_number((1, 3, 7, 12, 6))

'''Task 1.6
Write a program which makes a pretty print of a part of the multiplication table.'''
def mult_table(a,b,c,d):
    print("", *range(c, d+1, 1), sep='\t')
    for i in range(a, b+1):
        print(i, *range(i*c, i*d+1, i), sep='\t')

#mult_table(2,4,3,9)