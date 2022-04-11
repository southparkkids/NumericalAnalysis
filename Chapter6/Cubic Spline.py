#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[37]:


# Spline3_Coef pseudocode p.271
def Spline3_Coef(n, t, y, z):
    h = np.zeros(n-1)
    b = np.zeros(n-1)
    u = np.zeros(n-1)
    v = np.zeros(n-1)
    for i in range(0, n-1):
        h[i] = t[i+1] - t[i]
        b[i] = (y[i+1] - y[i])/h[i]
    u[1] = 2*(h[0] + h[1])
    v[1] = 6*(b[1] - b[0])
    for i in range(2, n-1):
        u[i] = 2*(h[i] + h[i-1]) - (h[i-1]**2/u[i-1])
        v[i] = 6*(b[i] - b[i-1]) - (h[i-1]*v[i-1]/u[i-1])
    z[n] = 0
    for i in range(n-2, 0, -1):
        z[i] = (v[i] - h[i]*z[i+1])/u[i]
    z[0] = 0
    return z


# In[38]:


# Spline3_Eval pseudocode p.271
def Spline3_Eval(n, t, y, z, x):
    for i in range(n-2, -1, -1):
        if x - t[i] >= 0:
            break
    h = t[i+1] - t[i]
    tmp = z[i]/2 + (x - t[i])*(z[i+1] - z[i])/(6*h)
    tmp = -(h/6)*(z[i+1] + 2*z[i]) + (y[i+1] - y[i])/h + (x - t[i])*tmp
    return y[i] + (x-t[i])*tmp


# In[39]:


X = np.zeros(20)
Y = np.zeros(20)
X = [0.0, 0.6, 1.5, 1.7, 1.9, 2.1, 2.3, 2.6, 2.8, 3.0, 3.6, 4.7, 5.2, 5.7, 5.8, 6.0, 6.4, 6.9, 7.6, 8.0]
Y = [-0.8, -0.34, 0.59, 0.59, 0.23, 0.1, 0.28, 1.03, 1.5, 1.44, 0.74, -0.82, -1.27, -0.92, -0.92, -1.04, -0.79, -0.06, 1.0, 0.0]
Z = np.zeros(21)
Spline3_Coef(20, X, Y, Z)

XS = np.arange(0, 8, 0.01)
YS = np.zeros(len(XS))
for i in range(0, len(XS)):
    YS[i] = Spline3_Eval(19, X, Y, Z, XS[i])
# 6.2 Figure 5.8

# Format plot figure
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

# Add f(x) line and points used by Simpson approximation
ax1.scatter(X,Y, label = 'y = S(x)')
ax1.plot(XS,YS, label = 'y = S(x)')
#ax1.scatter(XP,PP)

# Set title of plot
plt.title('f(x) = 1/(1+x^2) from 0 to 1')

# Give x axis label
plt.xlabel('x')
plt.ylabel('f(x)')

# Format the plot
plt.legend(loc='upper right')
plt.grid(True, which='both')
plt.axhline(y=0)
plt.show()


# In[41]:


# Test_Spline3 pseudocode p.272
n = 9
a = 0
b = 1.6875
h = (b - a)/n
t = np.zeros(n+1)
y = np.zeros(n+1)
for i in range(0, n):
    t[i] = a + i*h
    y[i] = np.sin(t[i])
z = np.zeros(n+1)
Spline3_Coef(n, t, y, z)
temp = 0
for j in range(0, 4*n):
    x = a + j*h/4
    e = np.abs(np.sin(x) - Spline3_Eval(n, t, y, z, x))
    if j == 19:
        print("j =", j, "\nx =", x, "\ne =", e)
    if e > temp:
        temp = e
    #print(j)
print("j =", j, "\nx =", x, "\ne =", e)
#Book solution j = 19, x = 0.890625, and d = 0.930 x 10^-5.


# In[56]:


def f(x):
    return (x**2 + 1)**(-1)
n = 41
t = np.linspace(-5, 5, n)
y = f(t)
print(t)
print(y)
z = np.zeros(n+1)
Spline3_Coef(n, t, y, z)
XS = np.linspace(0, 5, 101)
YS = np.zeros(len(XS))
for i in range(0, len(XS)):
    YS[i] = Spline3_Eval(40, t, y, z, XS[i])

# Format plot figure
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

# Add f(x) line and points used by Simpson approximation
ax1.scatter(t,y, label = 'f(x) = (x^2 + 1)^-1')
ax1.plot(XS,YS, label = 'S(x)')
#ax1.scatter(XP,PP)

# Set title of plot
plt.title('f(x) = 1/(1+x^2) from 0 to 1')

# Give x axis label
plt.xlabel('x')
plt.ylabel('f(x)')

# Format the plot
plt.legend(loc='upper right')
plt.grid(True, which='both')
plt.axhline(y=0)
plt.show()

Y = f(XS)
Dif = YS - Y
print(Dif)
print("Max difference: ", max(Dif), "\nAverage difference: ", np.average(Dif), "\nStandard Deviation: ", np.std(Dif))


# In[ ]:




