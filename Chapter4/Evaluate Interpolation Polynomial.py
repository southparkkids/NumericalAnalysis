#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#Evaluation of Interpolation Polynomial Pseudocode
def EvalInterpPoly(n,X,A):
    V = np.zeros(n)
    V = A[n]
    for i in range(n-1,0,-1):
        V = V*(t-X(i)) + A[i]
    return V


# In[2]:


#Devided Differences Pseudocode
def SlowDivDif(n,X,F):
    A = np.zeros(n)
    for i in range(0,n):
        A[i][0] = F(X[i])
    for j in range(1,n):
        for i in range(0,n-j):
            A[i][j] = (A[i+1][j-1] - A[i][j-1])/(X[i+j]-X[i])
    return A


# In[3]:


#Improved Devided Differences Pseudocode
def DivDif(n,X,F):
    A = np.zeros(n)
    for i in range(0,n):
        A[i] = F(X[i])
    for j in range(1,n):
        for i in range(n,j,-1):
            A[i] = (A[i] - A[i-1])/(X[i]-X[i-j])
    return A


# In[4]:


# Coef Pseudocode
def Coef(n,X,Y):
    A = np.zeros(n+1)
    for i in range(0,n+1):
        A[i] = Y[i]
    for j in range(1,n+1):
        for i in range(n,j-1,-1):
            A[i] = (A[i]-A[i-1])/(X[i]-X[i-j])
    return A


# In[5]:


# Eval Pseudocode
def Eval(n,X,A,t):
    temp = A[n]
    for i in range(n-1,-1,-1):
        temp = (temp)*(t-X[i])+A[i]
    Eval = temp
    return Eval


# In[6]:


#Test_Coef_Eval Pseudocode
n = 9
h = 1.6875/n
X = np.zeros(n+1)
Y = np.zeros(n+1)
for k in range(0,n+1):
    X[k] = k*h
    Y[k] = np.sin(X[k])
A = Coef(n,X,Y)
print("X: ",X,"\nY: ",Y,"\nA: ",A)
emax = 0
for j in range(0,4*n+1):
    t = j*h/4
    p = Eval(n,X,A,t)
    e = np.abs(np.sin(t)-p)
    if e > emax:
        jmax = j
        tmax = t
        pmax = p
        emax = e
print("jmax = ",jmax)
print("tmax = ",tmax)
print("pmax = ",pmax)
print("emax = ",emax)


# In[ ]:




