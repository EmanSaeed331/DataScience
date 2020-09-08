#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 04:17:27 2020

@author: eman-saeed
"""

"""
numpy documentation https://numpy.org/doc/stable/contents.html
"""

#Numpy is a firest data analysis library 
"""
Numpy is a linear algebrary for python , 
it's so important for data science with python  as  one of their main building blocks ,
Numpy is incredibly fast and has bindings to C libraries .
"""
#installing numpy 
"""
conda install numpy ,
pip install numpy
"""
"""
numpy arrays are the main way to work with arrays .

Numpy arrays essentially come in two flavors :
    1-vectors.
    2-metrices
    vectors are 1-d arrays.
    metrices are 2-d arrays.
    
arrays can be vectors (1-dimension) or metrices (2-dimension)
"""
import numpy as np
my_list = [1,2,3] 
arr = np.array(my_list)
print(arr) 

"""
to use a 2-d array we can cast a list of lists
"""

my_mat = [[2,4,5],[1,4,6],[1,3,5]]
mar=np.array(my_mat)
print(mar)


"""
the most common way to creating an array 
1- np.arrang (start,stop,steps)., arrange return numbers from start to stop 
   and a given step size. 
2- generate a zeros array -> np.zeros
3- generate an ones array ->np.ones
4-linspace-> it used for generating a metrics , it returnes evenly spaced numbers 
              over a specified interval , it's generate a 1-d array.
5-eye -> identity metrix it's basically a two dimensional square matrix ->meaning the number of reos is the same as number of coloumns,
6- np.random.rand() -> this is going to creat an array of the given shape
                       you pass in and it's going to populate it with 
                       random samples from a uniform distribution over 0 to 1.
                       and that means if i want just eight one dimensional array of random 
                       numbers uniformaly distributed from 0 to 1 i can pass in a single 
                       digit and i'll get back that one dimensional array.
                       if we want 2-d np.random.rand(4,4).
7- np.random.randn()
8- np.arange(25) -> it creates an array from 0~24
9- np.reshape : you must 
10- ranarr.max() -> it gives the max number in array
11- ranarr.min() -> it gives the min number in array.
12- ranarr.argmax() -> it shows the index of max number .
13- ranarr.argmin() -> it shows the index of min number.
14- arr.shape ->to print the shape.
15- arr.dtype -> for the datatype of array.
16- we can make a refrence for our self -> from numpy.random import randint
                                           randint(2,10)  



"""
x= np.arange(1,10,0.2)
print(x)

z = np.zeros((4,4))
print(z)

O = np.ones((3,4))
print(O)

L = np.linspace(0,5,100)
print(L)

E = np.eye(4)
print(E)

R=np.random.rand(5)
print(R)

RR = np.random.rand(4,4)
print(RR)


np.random.randn()

I = np.random.randint(1,100,10)
print(I)

ranarr = np.random.randint(0,50,10)
print(ranarr)


arr.reshape(3,1)

print(arr.max())
print(arr.min())

print(arr.argmax())
print(arr.argmin())

print(arr.shape)

#--------------------------------------------------------

#Numpy indexing and Selection
"""
to print array element -> array [start index: end index]

"""


array = np.arange(0,11)
print(array)

print(array[1:5])
print(array[:])
print(array[:4])
print(array[0:1])
print(array[5:0])


array[0:5]

arr = np.arange(0,11)
print(arr)

slice_of_arr = array[0:10]
slice_of_arr[:]= 99
print(slice_of_arr)
#---------------------------------------------------------------
#numpy operations
"""
1-Array with array.
2-Array with Scalars.
3-Universal Array Functions.
"""
"""
add 2 arrays -> element to element .
"""
ar1 = np.arange(0,11)
ar2 = np.arange(0,11)

print(ar1+ar2)
print(ar1-ar2)

print(ar1+100)
print(ar1-100)

print(ar1/ar2)
print(ar1 **2)

print(np.sqrt(arr)) 












