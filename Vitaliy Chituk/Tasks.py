'''Task 7.1
Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor.'''

class Open_file:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, mode=self.mode)
        except FileNotFoundError:
            print(f"File {self.filename} not found")
        else:
            return self.file

    def __exit__(self, type, value, traceback):
        if self.file:
            self.file.close()
            print(f"finish work with file {self.filename}")
        if type:
            print(f"Exception {type} with message: {value} \n Traceback: {traceback}")
        return True


#with Open_file("test_context.txt", mode="w") as f:
#    f.write("this is test")

'''Task 7.2
Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.'''

from contextlib import contextmanager, suppress

@contextmanager
def open_file(filename, mode="r"):
    file = 0
    try:
        file = open(filename, mode=mode)
        print(f"file {filename} opened")
        yield file
    except Exception:
        print(f"Oops, there is error with {filename}")
    finally:
        if file:
            file.close()
            print(f"finish work with file {filename}")


#with suppress(RuntimeError):
#    with open_file("test_context.txt", mode="r") as f:
#        text = f.read()
#        print(text)

'''Task 7.3
Implement decorator with context manager support for writing execution time to log-file. See contextlib module.'''

import time
from contextlib import ContextDecorator

class Time_log(ContextDecorator):

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Start")
        self.start = time.time()
        return self

    def __exit__(self, *exc):
        try:
            with open(self.filename, "w") as f:
                f.write(f"Function finished on {time.time() - self.start} sec\n")
                print("Finish")
        except Exception:
            print(f"Oops, there is error with {self.filename}")
        return True

@Time_log("timelog.txt")
def factorial():
    res = 1
    for i in range(1, 100000):
        res *= i

#factorial()

'''Task 7.4
Implement decorator for supressing exceptions. If exception not occure write log to console.'''

def suppress_exceptions(func):

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            pass
        else:
            print(f"Operation on function finished successfully")
            return result
    return wrapper

@suppress_exceptions
def type_err():
    print("start function")
    raise TypeError("Only integers are allowed")

#type_err()

'''Task 7.5
Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors. 
Custom exceptions must be derived from custom base exception(not Base Exception class).'''

class WrongAttribute(Exception):
    pass

class NumberTooSmall(WrongAttribute):
    pass

class NotAnInteger(WrongAttribute):
    pass

class NotANumber(WrongAttribute):
    pass

def check_number(number):
    try:
        number = float(number)
        if number != int(number):
            raise NotAnInteger("NotAnInteger")
        if number < 3:
            raise NumberTooSmall("NumberTooSmall")
        return number % 2 == 0
    except ValueError:
        raise NotANumber("NotANumber") from ValueError

#number = 2
#print(check_number(number))


'''Task 7.6
Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. 
For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all exceptions 
and print user friendly output.'''


def isPrime(number):
     if number == 0 or number == 1:
        flag = False
     elif number == 2:
        flag = True
     else:
        for i in range(2, number):
             if number % i == 0:
                 flag = False
                 break
             else:
                 flag = True
     return flag

def goldbach():
    while True:
        input_number = input("Please enter number or 'q' to quit: \n")
        if input_number == "q":
            break
        try:
            if check_number(input_number):
                number = int(input_number)
                for i in range(1, number):
                    k = number - i
                    if isPrime(i) and isPrime(k):
                        print(f"{number} = {i} + {k}")
                        break
            else:
                print("Number not even")
        except Exception as error:
            print(f"{error.__class__.__name__}")


#goldbach()

'''Task 7.7
Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. 
It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised. 
Method init sholud be able to take either 
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection 
or some ordered iterable collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
>>> [0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
>>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
>>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
>>> [0, 2, 4, 5, 7]
col2.append("string")
>>> TypeError: 'string' - object is not a number!
print(col1 + col2)
>>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
>>> [0, 2, 4, 5, 7]
print(col2)
>>> [1, 2, 3, 4, 5]
print(col2[4])
>>> 25
for item in col1:
    print(item)
>>> 0 2 4 5 7
```'''

class MyNumberCollection:

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], tuple):
                for i in args[0]:
                    if not isinstance(i, int):
                        raise TypeError('MyNumberCollection is not integer')
                self.items = list(args[0])
            elif isinstance(args[0], str):
                raise TypeError(f'{args[0]!r} - MyNumberCollection is string!')
        else:
            self.items = [x for x in range(args[0], args[1], args[2])]

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return str(list(self.items))

    def __add__(self, other):
        summ = self.items + other.items
        return MyNumberCollection(tuple(summ))

    def __getitem__(self, x):
        return self.items[x]

    def append(self, value):
        if isinstance(value, str):
            raise TypeError(f'{value!r} - MyNumberCollection is not integer')
        self.items.append(value)


#col1 = MyNumberCollection(0, 5, 2)
#print(col1)
#col2 = MyNumberCollection((1,2,3,4,5))
#print(col2)
#col1.append(7)
#print(col1)
#print(col1 + col2)
#print(col1)
#print(col2)
#print(col2[4])
#for item in col1:
#    print(item)

'''Task 7.8
Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.
Example:
```python
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
>>> 1 4 9 16 25

```'''

class MySquareIterator:
    def __init__(self, collect):
        self.collect = collect

    def __iter__(self):
        self.start = -1
        self.stop = len(self.collect) - 1
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += 1
            return self.collect[self.start] ** 2
        else:
            raise StopIteration

#lst = [1, 2, 3, 4, 5]
#itr = MySquareIterator(lst)
#for item in itr:
#    print(item, end=" ")


'''Task 7.9
Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.  
_Note: Do not use function `range()` at all_
Example:
```python
er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
```'''

class EvenRange:

    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start+1
        self.end = end
        self.flag = False

    def __iter__(self):
        self.flag = True
        return self

    def __next__(self):
        if self.start <= self.end:
            num = self.start
            self.start += 2
            return num
        elif self.flag:
            print("Out of numbers!")
            raise StopIteration
        else:
            return "Out of numbers!"

#er1 = EvenRange(7,11)
#print(next(er1))
#print(next(er1))
#print(next(er1))
#print(next(er1))

#er2 = EvenRange(3, 14)
#for number in er2:
#    print(number, end=" ")


'''Task 7.10
Implement a generator which will generate odd numbers endlessly.
Example:
```python
gen = endless_generator()
while True:
    print(next(gen))
>>> 1 3 5 7 ... 128736187263 128736187265 ...
```'''

def endless_generator():
    num = 1
    while True:
        yield num
        num += 2

#gen = endless_generator()
#while True:
#    print(next(gen))

'''Task 7.11
Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
Example:
```python
gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ...
```'''

def endless_fib_generator():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr


#gen = endless_fib_generator()
#while True:
#    print(next(gen))