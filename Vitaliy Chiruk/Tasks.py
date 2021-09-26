'''Task 4.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

Example:
```python
>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
Maximal value is reached.
>>> c.get()
43
```'''

class Counter:

    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop is None or self.start < self.stop:
            self.start += 1
        else:
            print("Maximal value is reached")

    def get(self):
        return print(self.start)

#c = Counter(start=42, stop=43)
#c.increment()
#c.get()
#c.increment()
#c.get()

'''Task 4.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.

Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()
["bar"]
```
<em>After your own implementation of the class have a look at collections.deque 
https://docs.python.org/3/library/collections.html#collections.deque </em>'''

class HistoryDict:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.history = []

    def set_value(self, key, value):
        self.dictionary[key] = value
        self.history = self.history[-9:] + [key]

    def get_history(self):
        print(self.history)

#d = HistoryDict({"foo": 42})
#d.set_value("bar", 43)
#d.get_history()

'''Task 4.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. 
until the keyword is used up, whereupon the rest of the ciphertext letters are used in 
alphabetical order, excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"
* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>
Example:
```python
>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"
>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```'''

from string import ascii_letters, ascii_lowercase

class Cipher:

    def __init__(self, secret_key):
        self.secret_key = "".join(sorted(set(secret_key), key=secret_key.index)).lower()
        #keyword in crypto
        self.secret_alphabet = self.secret_key + "".join(x for x in ascii_lowercase if x not in secret_key)
        self.secret_alphabet += self.secret_alphabet.upper()

    def encode(self, text):
        print(text.translate(str.maketrans(ascii_letters, self.secret_alphabet)))

    def decode(self, text):
        print(text.translate(str.maketrans(self.secret_alphabet, ascii_letters)))

#cipher = Cipher("crypto")
#cipher.encode("Hello world")
#cipher.decode("Fjedhc dn atidsn")

'''Task 4.4
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class.'''

class Bird:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} bird can walk and fly"

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")

class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def __str__(self) -> str:
        return f'{self.name} can walk and fly'

    def eat(self):
        print(f"It eats mostly {self.ration}")

class NonFlyingBird(Bird):

    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk and swim"

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def swim(self):
        print(f"{self.name} bird can swim")

class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name, ration="fish"):
        self.ration = ration
        NonFlyingBird.__init__(self, name, ration)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

    def fly(self):
        print(FlyingBird.fly(self))

#b = Bird("Any")
#b.walk()
#p = NonFlyingBird("Penguin", "fish")
#p.swim()
#p.fly()
#p.eat()
#c = FlyingBird("Canary")
#print(c)
#c.eat()
#s = SuperBird("Gull")
#print(s)
#s.eat()

'''Task 4.6
A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.
Example:
```python
>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True
```'''

class Sun:

    instance = None

    def __new__(cls):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance

    @classmethod
    def inst(cls):
        return cls.__new__(cls)

#p = Sun.inst()
#f = Sun.inst()
#print(p is f)

'''Task 4.7 
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}
```
Example:
```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>543.21 EUR
lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>123.45 BYN
```'''

class Money:

    exchange_rate = {
        'EUR': 0.85,
        'BYN': 2.5,
        'USD': 1,
        'JPY': 110.75
    }

    def __init__(self, value, currency='USD'):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f'{self.value:.2f} {self.currency}'

    def __repr__(self):
        return f'{self.__class__.__name__ }({self.value:.2f},{self.currency!r})'

    def __add__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return Money(self.value + other.value / rate, self.currency)

    def __iadd__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return Money(self.value + other.value * rate, self.currency)

    def __mul__(self, value):
        return Money(self.value * value, self.currency)

    def __rmul__(self, value):
        return Money(self.value * value, self.currency)

    def __sub__(self, other):
        return Money(self.value - other.value, self.currency)

    def __truediv__(self, other):
        return Money(self.value / other.value, self.currency)
    
    def __lt__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value < other.value / rate
    
    def __le__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value <= other.value / rate
    
    def __eq__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value == other.value / rate

    def __ne__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value != other.value / rate

    def __gt__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value > other.value / rate

    def __ge__(self, other):
        rate = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value >= other.value / rate


#x = Money(10, "BYN")
#y = Money(11) # define your own default value, e.g. “USD”
#z = Money(12.34 , "EUR")
#print(z + 3.11 * x + y * 0.8) # result in “EUR”

'''Task 4.8
Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.
Example:
```python
>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19
>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.'''

class Pagination:

    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.pages = [text[x:x+number] for x in range(0, len(text), number)]
        self.page_count = len(self.pages)
        self.item_count = len(text)

    def count_items_on_page(self, page):
        return len(self.pages[page])

#pages = Pagination('Your beautiful text', 5)
#print(pages.page_count)
#print(pages.item_count)
#print(pages.count_items_on_page(0))
#print(pages.count_items_on_page(3))
#pages.count_items_on_page(4)