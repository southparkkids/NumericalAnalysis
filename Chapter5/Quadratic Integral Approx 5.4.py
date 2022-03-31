#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Quadratic Integral Approximation 5.4
def GausIntegral(f, a, b, n):
    def g(t):
        return f(((b-a)*t+(b+a))/2) * ((b-a)/2)
    if n == 1:
        I = g(-(1/3)**0.5)             + g((1/3)**0.5)
        return I
    if n == 2:
        I = (5/9)*g(-(3/5)**0.5)             + (8/9)*g(0)             + (5/9)*g((3/5)**0.5)
        return I
    if n == 3:
        I = ((1/2)+(1/12)*((10/3)**.5))*g(-((1/7)*(3-4*(0.3**0.5)))**0.5)             + ((1/2)-(1/12)*((10/3)**.5))*g(-((1/7)*(3+4*(0.3**0.5)))**0.5)             + ((1/2)+(1/12)*((10/3)**.5))*g(((1/7)*(3-4*(0.3**0.5)))**0.5)             + ((1/2)-(1/12)*((10/3)**.5))*g(((1/7)*(3+4*(0.3**0.5)))**0.5)
        return I
    if n == 4:
        I = (0.3*((-0.7+5*(0.7**0.5))/(-2+5*(0.7**0.5))))*g(-((1/9)*(5-(2*(((10/7)**0.5)))))**0.5)             + (0.3*((0.7+5*(0.7**0.5))/(2+5*(0.7**0.5))))*g(-((1/9)*(5+(2*(((10/7)**0.5)))))**0.5)             + (128/225)*g(0)             + (0.3*((-0.7+5*(0.7**0.5))/(-2+5*(0.7**0.5))))*g(((1/9)*(5-(2*(((10/7)**0.5)))))**0.5)             + (0.3*((0.7+5*(0.7**0.5))/(2+5*(0.7**0.5))))*g(((1/9)*(5+(2*(((10/7)**0.5)))))**0.5)
        return I


# In[3]:


def f(x):
    return 1/(x**0.5)
a = 0
b = 1
I = GausIntegral(f, a, b, 1)
print(I)
print(I - 1.4183)
# Book solution of 1.4183 is wrong?


# In[4]:


# Example 3 approximation for e^(-x^2) from x = 0 to x = 1
def f(x):
    return np.exp(-(x**2))
a = 0
b = 1
I = GausIntegral(f, a, b, 2)
print(I)
print(I-0.746814584)
#Correct!!!


# In[ ]:




