# -*- coding: utf-8 -*-
"""Homework_2_Classes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l-9Hd6U8GrFFpNRjRE77SxW74Vqk00za

Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).

Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:
"""

NAME = "Yash Sharma"
COLLABORATORS = "None"

"""---

# Homework 2: Classes
## CSE 30 Winter 2021

## Luca de Alfaro
Copyright Luca de Alfaro, 2020.  CC-BY-NC License.

# Instructions

## The Format of a Python Notebook

*This* is a Python Notebook homework.  It consists of various types of cells: 

* Text: you can read them :-) 
* Code: you should run them, as they may set up the problems that you are asked to solve.
* **Solution:** These are cells where you should enter a solution.  You will see a marker in these cells that indicates where your work should be inserted.  

```
    # YOUR CODE HERE
```    

* Test: These cells contains some tests, and are worth some points.  You should run the cells as a way to debug your code, and to see if you understood the question, and whether the output of your code is produced in the correct format.  The notebook contains both the tests you see, and some secret ones that you cannot see.  This prevents you from using the simple trick of hard-coding the desired output.

## Running your notebook

**Running a cell.**
To run a cell of the notebook, either click on the icon to its top left, or press shift-ENTER (or shift-Return). 

**Disconnections.**
When you open a notebook, Google automatically connects a server to the web page, so that you can type code in your browser, and the code is run on that server.  If you are idle for more than a few minutes, Google keeps all you typed (none of your work is lost), but the server may be disconnected due to inactivity.  When the server is disconnected, it loses all memory of anything you have defined (functions, classes, variables, etc). 

If you do get disconnected, select Runtime > Run All (or Runtime > Run before) to ensure everything is defined as it should. 

### DO NOT

* **Do not add, delete, reorder, remove cells.**  This breaks the relationship between your work, and the grading system, making it impossible to grade your work.

### Debugging
To debug, you can add print statements to your code.  They should have no effect on the tests.  Just be careful that if you add too many of them inside loops and similar, you may cause for some of the tests we will do such an enormous amount of output that grading might timeout (and you may not get credit for an answer). 

### Asking for help
The tutors and TAs should have access to the notebook; otherwise, you can always share a link with them.  In this way, they can take a look at your work and help you with debugging and with any questions you might have.

## Submitting Your Notebook

To submit:
* **Check your work.** Before submitting, select Runtime > Run All, and check that you don't get any unexpected error. 
* **Download the notebook.** Click on File > Download .ipynb . **Do not download the .py file.**
* **Upload.** Upload the .ipynb file to **[this Google form](https://docs.google.com/forms/d/e/1FAIpQLSd5Z4jCk0BYdz_Z8_eXS2rDl4EivmQVzSfC-AjhL0HcBEqMDw/viewform?usp=sf_link)**.

## The Test

There are 3 questions, for a total of 60 points.

## Question 1: Inheritance

Here is a class `BagOfWords` that implements the [bag of words](https://en.wikipedia.org/wiki/Bag-of-words_model) model of text, or a simplification of it, in any case.  You create a bag of words by passing to it a text string, like: 

    bag = BagOfWords("Hello I would like to travel to Naples, is Vesuvius erupting?")
    
and then you can ask how many times a word occurred in the text string:

    bag.occurrences("to")
    
Note that I am using a [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict), which is a dictionary where keys that are not found are associated with a default value (in this case, 0, as it is initialized as `defaultdict(int)`).
"""

from collections import defaultdict

class BagOfWords(object):

    def __init__(self, text):
        words = self._text_split(text)
        self.counts = defaultdict(int)
        for w in words:
            self.counts[w] += 1

    def occurrences(self, word):
        return self.counts[word]

    def _text_split(self, text):
        return text.split()

bag = BagOfWords("Hello I would like to travel to Naples, is Vesuvius erupting?")
bag.occurrences("to")

"""This works, but it's really a bit rudimentary; for instance: """

bag.occurrences("Naples")

"""The problem here is that the `.split()` function splits according to whitespace, and so the bag of words does not contain `"Naples"`, but `"Naples,"`, including the comma.  Here is a function that splits text in a better way, taking care of eliminating punctuation, and also turns words into lowercase.  It uses [regular expressions](https://docs.python.org/3/library/re.html). """

import re

def split_into_words(text):
    return [w.lower() for w in re.findall(r"[\w']+", text)]

split_into_words("Hello I would like to travel to Naples, is Vesuvius erupting?")

"""Ok, this works better.  Now here is the challenge: write a subclass `BetterBag` of `BagOfWords` that uses this function, instead of `.split()`, to split text into words. 
There are two ways of doing this.  One is to do it... brute force.  But the real challenge is: 

_Can you do it without writing the `__init__` method for `BetterBag`?  Can you do it so that all you need is 2 lines of code?_ 

Think about it.  You don't lose points by using a more verbose or less elegant solution.  But try to think at how you could do it.  And btw, do use my function `split_into_words` unchanged, otherwise some test might fail.
"""

class BetterBag(BagOfWords):
    def _text_split(self, text):
      return split_into_words(text)

# This is a place where you can write additional ctests to help you test 
# your code, or debugging code, if you need.  You can also leave it blank.

"""Let's check that `BetterBag` works as intended."""

# Let me define the function I use for testing.  Don't change this cell. 

def check_equal(x, y, msg=None):
    if x == y:
        if msg is None:
            print("Success")
        else:
            print(msg, ": Success")
    else:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

bb = BetterBag("Hello I would like to travel to Naples, is Vesuvius erupting?")
check_equal(bb.occurrences("naples"), 1)
check_equal(bb.occurrences("i"), 1)
check_equal(bb.occurrences("to"), 2)

"""
## Question 2: Modulo Arithmetic

We will implement a class `ModInt` that implements integers with a specified modulus. 
We can then create numbers modulo 7 using: 

    x = ModInt(7, modulus=10)
    y = ModInt(5, modulus=10)
    
and if we do `x + y`, we should obtain a number that is equal to `ModInt(2, modulus=10)`, because: 

$$
(5 + 7) \mod 10 = 12 \mod 10 = 2. 
$$

In other words, to compute $x \oplus y$ for $x, y$ that are `ModInt`, you do like this: 

* First, you check that both $x$ and $y$ share the same modulus (10 in the example above); if they do not, you raise a `TypeError` exception. 
* Second, you compute $x \oplus y$ as if $x$ and $y$ were integers, and then you compute the result $\mod n$, where $n$ is the _common_ modulus of $x$ and $y$. 

Some implementation notes:  

* To compute $x \mod n$, you write in Python `x % n`. 

* To raise a `TypeError`, you can simply do: 

    raise TypeError("Operation between numbers with different modulus")
  
* We will have you implement only the `+`, `-`, `*` operators, as well as the integer division `//`, which is implemented via the [`__floordiv__` operator](https://docs.python.org/3/reference/datamodel.html#object.__floordiv__). 

You might want to refer to the implementation of `Complex` in the class book chapter for an example. """

x = 5 // 3
print(x)

class ModInt(object):
    def __init__(self, x, modulus = 10):
        """Creates an integer with a specified modulus."""
        assert modulus > 0
        self.x = x % modulus
        self.modulus = modulus
    
    def __eq__(self, other):
        """We define equality, so that we can easily write tests."""
        return self.x == other.x and self.modulus == other.modulus
        
    def __repr__(self):
        """To print them in a meaningful way"""
        return "({} mod {})".format(self.x, self.modulus)

    def __add__(self, other):
        if self.modulus != other.modulus:
          raise TypeError("Operation between numbers with different modulus")
        return ModInt(self.x + other.x, self.modulus)   

    def __sub__(self, other):
        if self.modulus != other.modulus:
          raise TypeError("Operation between numbers with different modulus")
        return ModInt(self.x - other.x, self.modulus)
    
    def __mul__(self, other):
        if self.modulus != other.modulus:
          raise TypeError("Operation between numbers with different modulus")
        return ModInt(self.x * other.x, self.modulus)

    def __floordiv__(self, other):
        if self.modulus != other.modulus:
          raise TypeError("Operation between numbers with different modulus")
        return ModInt(self.x // other.x, self.modulus)

# This is a place where you can write additional tests to help you test 
# your code, or debugging code, if you need.  You can also leave it blank.

"""Here are some tests. """

## 5 points: tests for addition.

check_equal(ModInt(6) + ModInt(7), ModInt(13))
# Modulus 5 should also work. 
check_equal(ModInt(2, modulus=5) + ModInt(4, modulus=5), ModInt(1, modulus=5))

### 10 points: tests for the other operations

check_equal(ModInt(4) * ModInt(8), ModInt(2))
check_equal(ModInt(9, modulus=7) - ModInt(3, modulus=7), ModInt(6, modulus=7))
check_equal(ModInt(1, modulus=7) - ModInt(3, modulus=7), ModInt(-2, modulus=7))
check_equal(ModInt(70, modulus=43) // ModInt(8, modulus=43), ModInt(3, modulus=43))

### 10 points: sanity checks. 

x = ModInt(5)
y = ModInt(6)
z = x + y
check_equal(x, ModInt(5))
check_equal(y, ModInt(6))
check_equal(z, ModInt(1))

### 5 points: raising TypeError

raised = False
try:
    x = ModInt(4, modulus=6) + ModInt(5, modulus=7)
except TypeError:
    raised = True
check_equal(raised, True)

raised = False
try:
    x = ModInt(4, modulus=6) * ModInt(5, modulus=7)
except TypeError:
    raised = True
check_equal(raised, True)

"""## Question 3: Implementing a History Dictionary

In this question, you have to implement a dictionary that keeps the history of values that have been associated with each key.  You initialize the dictionary via: 

    d = HDict()

then you can update it via: 

    d['cat'] = 4
    d['dog'] = 6
    d['cat'] = 32 # This updates what was assigned to the key 'cat'
    
and you can retrieve the histories for each key via: 

    d.history('cat')
    
which yields the list of values assigned to key `'cat'` in chronological order: 

    [4, 32]
    
and `d.history('dog')`, which yields simply `[6]` as the key `'dog'` was only assigned to value `6`. 

To implement this, you might want to look at the book chapter on classes, and specifically, at the timestamped dictionary example. 
In implementing it, you can assume that one never passes anything to the initializer. 
My implementation consists of 10 lines of code.
"""

class HDict(object):
    
    def __init__(self):
        self.d = {}
        self.h = {}

    def __setitem__(self, k, v):
        self.d[k] = v
        if k in self.h:
          self.h[k].append(v)
        else:
          index = list(self.d.keys()).index(k)
          self.h[k] = []
          self.h[k].append(v)
          
    def __getitem__(self, k):
        return self.d[k]

    def history(self, k):
        return self.h[k]

d = HDict()
d['cat'] = 4
print(d)

# This is a place where you can write additional tests to help you test 
# your code, or debugging code, if you need.  You can also leave it blank.

"""Here are some tests. """

### 10 points: remembering the values. 

d = HDict()
d['cat'] = 4
check_equal(d['cat'], 4)
d['dog'] = 5
check_equal(d['dog'], 5)
check_equal(d['cat'], 4)
d['cat'] = 6
check_equal(d['dog'], 5)
check_equal(d['cat'], 6)

## 10 points: remembering history.

d = HDict()
d['cat'] = 4
d['dog'] = 5
d['cat'] = 6
check_equal(d.history('dog'), [5])
check_equal(d.history('cat'), [4, 6])