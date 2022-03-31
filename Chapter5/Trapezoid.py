#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[12]:


#Trapezoid from book p.204
def Trapezoid(n, f, a, b):
    h = (b-a)/n
    sum1 = (0.5)*(f(a)+f(b))
    for i in range(1,n):
        x = a + i*h
        sum1 = sum1 + f(x)
    sum1 = sum1*h
    return sum1


# In[13]:


def f(x):
    return 1/(np.exp(x**2))
n = 60
a = 0
b = 1
print(f(a))
print(f(b))
I = Trapezoid(n,f,a,b)
print(I)


# In[ ]:




