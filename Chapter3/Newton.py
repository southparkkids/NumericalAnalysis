#!/usr/bin/env python
# coding: utf-8

# In[17]:


def Newton(f,Df,x,nMax,epsilon,delta):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    fx = f(x)
    print("n\t x\u2099\t f(x\u2099)")
    print(0,"\t",x,"\t",fx)
    for n in range(1,nMax):
        fp = Df(x)
        if abs(fp) < delta:
            print("Small derivative!")
            break
            return None
        d = fx/fp
        x = x-d
        fx = f(x)
        print(n,"\t",x,"\t",fx)
        if abs(d) < epsilon:
            print("Convergence")
            break
            return None


# In[19]:


nMax = 6
def f(x):
    return ((x-2)*x+1)*x-3
def Df(x):
    return (3*x-4)*x+1
x = 3.0
epsilon = 1/2 * 10**(-6)
delta = 1/2 * 10**(-6)
Newton(f,Df,x,nMax,epsilon,delta)


# In[ ]:




