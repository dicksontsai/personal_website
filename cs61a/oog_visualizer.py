def oog_visualizer(func):
    """
    A function that helps visualize the number of recursive calls a function takes.

    Takes in a function.
    Returns a function that, when called, starts a new counter. Bind the function
    returned by the counter to the original name of the passed in function.

    Now when you call the overwritten original function, you should see how many
    recursive calls that function call will make with your specific input.
    >>> def spam(n):
    ...     for i in range(n):
    ...         for j in range(i):
    ...             return spam(n-1)
    ...
    >>> spam_visualizer = oog_visualizer(spam)
    >>> spam_counter = spam_visualizer()
    >>> spam = spam_counter
    >>> spam(100)
    100
    """
    def counter():
        count = 0
        def counted_func(*args):
            nonlocal count
            count += 1
            func(*args)
            
            return count
        return counted_func
    return counter

def spam(n):
    for i in range(n):
        for j in range(i):
            return spam(n-1)

def bar(n):
    if n == 3:
        return 'three!'
    for i in range(n // 2):
        bar(3)

def foo(n):
    times_table = [ n * i for i in range(1, 11)]
    for num in times_table:
        print(num)
"""
if __name__ == "__main__":
    counter_spam = oog_visualizer(spam)
    spam = counter_spam()
    print(spam(100))
"""
