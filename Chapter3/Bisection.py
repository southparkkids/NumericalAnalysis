#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Bisection(f,a,b,nMax,epsilon):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    nmax : (positive) integer
        The number of iterations to implement.
    epsilon : The error of our bisection or the range to stop the bisection at.
    '''
    fa = f(a)
    fb = f(b)
    if f(a)*f(b) >= 0:
        print(a,b,fa,fb)
        print("The function has the same signs at a and b!")
        return None
    if abs(a-b) < epsilon:
        print("The provided range is less than the provided error!")
        return None
    error = b-a
    print("n \t c\u2099 \t f(c\u2099) \t error")
    for n in range(0,nMax):
        error = error/2
        c = a + error
        fc = f(c)
        print(n,"\t",c,"\t",fc,"\t",error)
        if abs(error) < epsilon:
            print("Convergence")
            return a
            break
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc


# In[2]:


nMax = 20
epsilon = 1/2 * 10**(-6)
def f(x):
    return x**3 - 3*x +1
def g(x):
    return x**3 - 3*x +1
a = 0.0
b = 1.0
Bisection(f,a,b,nMax,epsilon)
print()
a = 0.5
b = 2.0
Bisection(g,a,b,nMax,epsilon)


# In[3]:


f = lambda x: x**2 - x - 1
approx_phi = Bisection(f,1,2,25,0.000000000001)
print(approx_phi)


# In[ ]:




