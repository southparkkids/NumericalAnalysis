#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.10g" % x))


# In[2]:


#Romberg from book p.219
def Romberg(f, a, b, n):
    R = np.array([[0.0]*n]*n, float)
    h = b - a
    R[0][0] = (h/2) * (f(a) + f(b))
    for i in range(1,n):
        h = h/2
        sum1 = 0
        for k in range(1,2**(i)+1, 2):
            sum1 = sum1+f(a+(k*h))
        R[i][0] = (1/2)*R[i-1][0] + sum1*h
        for j in range(1,i+1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1])/(4**(j) - 1)
    return R


# In[3]:


#test integral
def f(x):
    return 4/(1+x**2)
a = 0
b = 1
n = 5
print(Romberg(f,a,b,n))


# In[ ]:




