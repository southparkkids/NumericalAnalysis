#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def Gauss(n, A):
    X = np.zeros(n,dtype=float)
    L = np.arange(n,dtype=int)   #index vector
    S = np.zeros(n,dtype=float)
    for i in range(0, n):
        L[i] = i
        smax = 0
        for j in range(0, n):
            smax = max(smax, np.abs(A[i][j]))
        S[i] = smax
    for k in range(0, n-1):
        rmax = 0
        for i in range(k, n):
            r = np.abs(A[L[i]][k]/S[L[i]])
            if r > rmax:
                rmax = r
                j = i
        temp = L[j]
        L[j] = L[k]
        L[k] = temp
        for i in range(k+1, n):
            xmult = A[L[i]][k]/A[L[k]][k]
            A[L[i]][k] = xmult
            for j in range (k+1, n):
                A[L[i]][j] = A[L[i]][j] - (xmult*A[L[k]][j])
    return X,A,L


# In[3]:


def Solve(n,A,L,B,X):
    for k in range(0, n-1):
        for i in range(k+1, n):
            B[L[i]] = B[L[i]]-(A[L[i]][k]*B[L[k]])
    X[n-1] = B[L[n-1]]/A[L[n-1]][n-1]
    for i in range(n-1, -1, -1):
        sum1 = B[L[i]]
        for j in range(i+1, n):
            sum1 = sum1-A[L[i]][j]*X[j]
        X[i] = sum1/A[L[i]][i]
    return X


# In[4]:


def FullGauss(n,A,B):
    X,A,L = Gauss(n, A)
    X = Solve(n,A,L,B,X)
    return X


# In[5]:


#Example
A = np.array([[3.0, 4, 3],
              [1, 5, -1],
              [6, 3, 7]])
B = np.array([10.0, 7, 15])
print(A, "\n")
print(B, "\n")

n = 3
X,A,L = Gauss(n,A)
X = Solve(n,A,L,B,X)
print("Solution ", X)
#solution [2,1,0]

