
# coding: utf-8

## Discussion 10 Warmup 7/24/14

### OOP and Inheritance - What Will Python Print?

# OOP environment diagrams will not be tested, but What will Python Print questions will certainly appear. After you are done, document your reasoning behind your answers. Then, please try running this code in PythonTutor so that you can make sure that you are correctly visualizing the execution of OOP code. 
# Fill out the "# In[ ]" parts with the actual output from the interpreter.


class A:
    print(2)
    smart = 2
    def __init__(self):
        self.classy = True


# In[ ]:

class B(A):
    def __init__(self):
        print(5)
        self.smart = 3
    def revert(self):
        A.__init__(self)


# In[ ]:

b = B()


# In[ ]:

b.classy


# In[ ]:

b.revert()


# In[ ]:

b.classy

# In[ ]:

### Iterators

# Write a function `multiples` that returns an iterator that yields every multiple of n. For example, `multiples(2)` will become an iterator of evens: 0, 2, 4, .... 
# 
def multiples(n):`
    """
    >>> a = multiples(3)
    >>> for i in range(5)
    ...   print(next(a))
    0
    3
    6
    9
    12
    """
