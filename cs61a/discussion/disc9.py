
# coding: utf-8

## Discussion 9 Warmups 7/22

### What Would Python Print?

# Try to explain everything using environment diagrams. You will not be tested on OOP environment diagrams, but they are important to help you visualize what's going on. You should document the reasoning behind your answers, and then re-adjust your reasoning as you go over your answers with PythonTutor
# Fill out the "# In[ ]" parts with the actual output from the interpreter.

class A:
  def __init__(self, id):
    self.id = id
  def print_id(self):
    print(self.id)


# In[ ]:

A


# In[ ]:

a = A(5)
a.print_id


# In[ ]:

A.print_id


# In[ ]:

A.print_id(self)


# In[ ]:

A.print_id()


# In[ ]:

A.print_id(a)


# In[ ]:

a.print_id = lambda self: print(self.id)
a.print_id()


# In[ ]:

a.print_id(a)


# In[ ]:

a.print_id(A(2))


# In[ ]:

A.classy = False
a.classy


# In[ ]:

a.classy = True
A.classy


# In[ ]:

a.classy


# In[ ]:

B = A
B.classy

# In[ ]:
