#!/usr/bin/env python
# coding: utf-8

# In[6]:


def Secant(f,a,b,nMax,epsilon):
    fa=f(a)
    fb=f(b)
    if abs(fa) > abs(fb):
        atemp = a
        fatemp = fa
        a = b
        b = atemp
        fa = fb
        fb = fatemp
        return None
    print(0,a,fa)
    print(1,b,fb)
    for n in range(2,nMax):
        if abs(fa) > abs(fb):
            atemp = a
            fatemp = fa
            a = b
            b = atemp
            fa = fb
            fb = fatemp
        d = (b-a)/(fb-fa)
        b = a
        fb = fa
        d = d*fa
        if abs(d) < epsilon:
            print("Convergence")
            print(n,a,fa)
            break
            return None
        a = a-d
        fa = f(a)
        print(n,a,fa)


# In[8]:


def p(x):
    return x**5 + x**3 +3
a = -1
b = 1
nMax = 20
epsilon = 1/2 * 10**(-16)
Secant(p,a,b,nMax,epsilon)


# In[ ]:




