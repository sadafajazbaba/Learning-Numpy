# -*- coding: utf-8 -*-
"""Numpy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-FpjeBsUhKLu9DG3diG9Fpqg-3foWQCN
"""

import numpy as np
a = np.array([1,2,3,4])
a +1 #scaler edition

a **2

b = np.ones(4) +1
a-b
a*b

c = np.diag([1,2,3,4])
print(c*c)
print(c.dot(c))

a = np.array([1,2,3,4])
b =np.array([5,2,2,4])
c= np.array([1,2,3,4])
a ==b
a >b
np.array_equal(a,c)

a = np.array([1,1,0,0],dtype=bool)
b = np.array([1,0,1,0],dtype=bool)
np.logical_or(a,b)

a = np.arange(5)
np.sin(a)
np.log(a)
np.exp(a)

x = np.array([1,2,3,4])
np.sum(x)

x =np.array([[1,1],[2,2]])
x.sum(axis=0) #column wise sum    #axis =1 row wise sum

x = np.array([1,2,3,4])
x.min()
x.max()
x.argmin() #index of minimum element
x.argmax() #index of max element

np.all([True,True,False])

np.any([True,True,False])

a = np.zeros((50,50))
np.any(a!=0)
np.all(a==a)
a.mean()
np.median(a)
#axis = -1 also signifies rows

data = np.loadtxt('p')