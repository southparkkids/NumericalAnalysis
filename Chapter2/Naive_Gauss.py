#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Naive_Gauss Pseudocode copied
import numpy as np
import sys


# In[2]:


#Naive_Gauss Pseudocode For Python
def Naive_Gauss(A, B):
    n = len(B)
    # Elimination phase
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k]/A[k,k]
                A[i,k+1:n] = A[i,k+1:n] - lam*A[k,k+1:n]
                B[i] = B[i] - lam*B[k]
    # Back substitution
    for k in range(n-1, -1, -1):
        B[k] = (B[k] - np.dot(A[k,k+1:n],B[k+1:n]))/A[k,k]
    return B


# In[3]:


A = np.array([[2, 1, 1],
              [-1, 1, -1],
              [1, 2, 3]], dtype = float)

B = np.array([2, 3, -10], dtype = float)
X = Naive_Gauss(A, B)
print(X)
#answer [3,1,-5]


# In[4]:


A = np.array([[2, 1, 1, 2],
              [-1, 1, -1, 3],
              [1, 2, 3, -10]], dtype = float)
rows = np.shape(A)[0]
cols = np.shape(A)[1]
print(rows)
print(cols)


# In[9]:


m = 10
#A = np.array(zeros_like)
#B = np.array(zeros_like)
A = np.arange(m*m,dtype=float).reshape(m, m)   #, dtype=np.int32
B = np.arange(10,dtype=float)
print(A)
print(B)
for n in range(4,m):
    for i in range(1,n):
        for j in range(1,n):
            A[i][j] = (i+1)**(j-1)
        B[i] = (((i+1)**n)-1)/i
print("\n",A,"\n",B)
X = Naive_Gauss(A,B)
print("\n",X)


# In[10]:


A = np.array([[1.0, 0, 3],
              [0, 1, -3],
              [3, -3, 0],
              [0, 2, 4]])
B = np.array([0.0, 0, 6, -6])
print(A, "\n")
print(B, "\n")

X = Naive_Gauss(A,B)
print(X,"\n")


# In[ ]:




