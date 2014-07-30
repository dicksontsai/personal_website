
# coding: utf-8

## Mutation Practice Problems

### Basic Concepts

# 1. If mutation did not exist, what would Python have to do every time it wanted to add an element to a list?
# 2. If the bindings on frames are key-value pairs, what is the key and value of the binding created with this line? Then, describe in your own words how aliasing works. What would happen if I used the value of `a` in a call expression? What gets bound to the formal parameter in the new frame?
# 
#     `a = [1, 2, 3]`  
# 3. Are `map`, `filter`, and `reduce` mutating functions?

### Start Simple

# Make sure you know how to visualize the basic data types. These examples will help you get started. Remember, <a href="pythontutor.com/visualize.html">PythonTutor</a> is your friend.

# In[ ]:

# Lists
a = [1, 2, 3]
# Look up elements using []
print(a[0])
print(a[1])
b = a.pop()
a.extend([5])
# Reassign an element
a[0] = 0

# Compare with the corresponding immutable code
c = [1, 2, 3]
# Slicing makes a new copy. Does not modify the original list
d, e = c[:2], c[2]
c = c + [5]
c = [0] + c[1:]


# In[ ]:

# Tuples
# A one-element tuple is represented by a comma, e.g. a tuple with 5 only is (5,)
a = (1, 2)
b = (3,)
c = a + b
print(c[2])
# Note that tuples are immutable. What do a, b, and c point to?


# In[ ]:

# Dictionaries
a = {} # Empty dictionary
# Add new item
a[1] = 2
# Look up item
print(a[1])
# Update item
a[1] = True

a[2] = False
# Delete item
del a[1]
print(a)


### Exploration

# Once you understand the basic building blocks, you should start to experiment by combining these concepts together, along with concepts covered previously), in as many ways as you can. Here are some examples to get you started:
# 1. *(Lists + functions)* Make a list of multipliers, one-argument functions: e.g. a list `a` such that `a[0](12)` is 0, `a[1](12)` is 12, `a[2](2)` is 24, etc.
# 2. *(Dictionaries + lists)* Make a dictionary where one item has a list as a value. How do you index that list via a dictionary?
# 3. *(Trees + tuples)* Recall the code for functional trees. Create a tree where each datum is a tuple. How does this change make the tree more powerful than before?

### What Would Python Print?

# In[ ]:

a = [1, 2, 3]
b = a
b[2] = a[1]
a[0] = a
a is b


# In[ ]:

a[0] is b


# In[ ]:

b = a[:]
a is b


# In[ ]:

a[0] is b


# In[ ]:

a is b[0]


# Now try coming up with some of your own code. Play around with all the tools you have. Let the interpreter answer your questions and (hopefully) fuel your fascination for how Python works.

### Environment Diagrams

# Try drawing out an environment diagram to the above WWPP code. Notice that once we have access to an object, we can invoke methods on that object to modify it. It's important to be able to visualize what is going on.

# In[ ]:

def make_buffer():
    buff = []
    def buffer_in(x):
        buff.append(x)
        if len(buff) > 1:
            output = buff
            buff = []
            return output
    return buffer_in
my_buff = make_buffer()
my_buff('hello,')
my_buff('world!')


# **Followup**: Does the code above run properly? If so, explain how it works. If not, explain the change(s) you would have to make.

# In[ ]:

a = {1: 2}
b = ['hello', {5: 6, 7: 8}, (2, 3)]
a[1] = b
a[b[2]] = a[1][2]
b[2] = (5, 6)
a[1].remove('hello')
a[(2, 3)]
a[a[1][1]]


### Basic Practice Problems

# 1. Define a function `inc_index`, that, given a list of numbers and an index, increments the number at the index in the original list. Do not make a new list.

# In[ ]:

def inc_index(lst, index):
    """
    Increment the element at index of lst by 1.
    >>> a = [1, 2, 3]
    >>> inc_index(a, 2)
    >>> a
    [1, 2, 4]
    """


# `2.` Now we're going to play a bigger trust game: Implement `deep_inc_index` which either increments the number at that index or, if a list is at that index, applies this function recursively.

# In[ ]:

def deep_inc_index(lst, index):
    """
    Increment the element at index of lst if that element is a number or else recurse.
    >>> a = [1, [2, [3, 4], 5], 4]
    >>> deep_inc_index(a, 1)
    >>> a = [1, [2, [3, 5], 5], 4]
    """


### Advanced Practice Problems

# `1.` Define a function `clean_dict` that takes in a dictionary and an object and removes any entries that match the object's type. Do this recursively if the value of a key is also a dictionary:

# In[ ]:

def clean_dict(target_dict, obj):
    """
    >>> a = {1: {2: True, 3: "happy"}, 4: False, 5: "and you", 6: {7: {8: "know it"}, 9: True}}
    >>> clean_dict(a, 1 > 2)
    >>> {1: {3: "happy"}, 5: "and you", 6: {7: {8: "know it"}}}
    """


# `2.` Given a list of two-argument functions and a list of arguments, write a function that returns dictionary that maps the function to the result of evaluating it with the given arguments. Any arguments not used can be safely ignored. If there are not enough arguments, raise an error.

# In[ ]:

def dict_results(lst_fn, *args):
    """
    >>> adder, subber, muller, power = lambda x, y: x+y, lambda x, y: x-y, lambda x, y: x * y, lambda x, y: x ** y
    >>> math_lst = [adder, subber, muller, power]
    >>> output = dict_results(math_lst, *range(10))
    >>> output[adder] # 0 + 1
    1
    >>> output[subber] # 2 - 3
    -1
    >>> output[muller] # 4 * 5
    20
    >>> output[power] # 6 ** 7
    279936
    >>> output = dict_results(math_lst, *range(4))
    Traceback (most recent call last):
        ...
    TypeError: not enough arguments
    """


# Now, you should try to write functions that can mutate trees. Note that since trees are recursive data structures, you can mutate them recursively just as in the first advanced problem. One important point of mutation is: **Now that there are side effects, you can no longer just consider input and output. You HAVE to consider what the function does, and trust that the function does what it says it does, as you recurse.**
