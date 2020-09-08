#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""


#Data visualizing by using matplot
"""
1-Matplotlib is the most popular plotting library.
2-it gives you control over every aspect of a figure.
3-it was designed to have a similar feel to MatLab's graphical plotting
"""
#install of Matplotlib 
"""
1-conda install matplotlib 
(or)
2-pip install matplotlib
"""
"""
official website for matplot -> https://matplotlib.org/
"""
#Matplot part1 
"""
1-matplot is called matplotlib .
2- import the library after installing.
3- basic matplot lib commands allow you to very quickly create a plot .


"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2
print(y)

#Functional method 
"""
4- there is two ways to create a matplotlib :
    1-one is a functional method .
    2-the other is object oriented method.
- there are a several arguments to plt.plot() - > shift+tab to show required elements
- we can choose the line style as the thired argument in plt.plot.
- we can use xlabel by -> plt.xlabel .
- we can use ylabel by -> plt.ylabel .
- we can make a title by ->plt.title
    """
plt.plot(x,y)
plt.show()
plt.plot(x,y,'g-')
plt.plot(x,y,'r-')
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')
plt.title('Title')
"""
- we can continue on creating multi plots on the same canvas by plt.subplot.
- plt.subplot -> takes in couple of arguments :
    1-number of rows.
    2-number of column.
    3-plot number you're referring to .
"""
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(y,x,'b')



#we are going to know more libs in object oriented API method.

"""
The main idae in using the more formal object orientedd method is to create figure objects
and then call methods off of this.
- we have a figure object , it has been created this figure object you just imaging a blank canvas.
- we can add a set of axes to this canvas  -> axes = fig.add_axes([])
- we are going to add a set of axes , 
  the way to add a set of axes is by passing  in a list 
  and the list will take four arguments:
      1- the left of the axes.
      2- the bottom of the axes.
      3- the width of the axes.
      4-the hieght of the axes.
- we create a figure mannually by add the axes and choose its location and size
  by using the plt.figure .
  
"""

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel("X label")
axes.set_ylabel("Y label")
axes.set_title("Title")

fig2 = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.15,0.4,0.3])
axes1.plot(x,y)
axes2.plot(x,y)
axes1.set_title("Larger PLOT")
axes2.set_title("Smaller plot")

#----------------------------------------------------------
#Matplot part2
"""
axes is a matplotlib essentially it's just a list of these axes obeject meaning.
"""

fig,axes = plt.subplots(nrows =1, ncols = 2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)

#Figure Size and DPI 
"""
- we start speaking about figure size aspect the ratio and DPI map .
- matplot lib allows ypu to control each of these aspects .
- DPI is dots per inch or pixels per inch.


"""
fig2 = plt.figure(figsize=(2,2),dpi =100)
ax = fig2.add_axes([0,0,1,1])
ax.plot(x,y)

fig1,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()

#Save a figure
"""
- fot saving a figure we use matplotlib to generate just high qulity outputs
  in a number of formats incuding : 
      1-PNG
      2-JPG
      3-SPG
      4-PDF
"""
fig.savefig('my_picutre.png',dpi=200)
ax = fig.add_axes([0,0,1,2])
ax.set_title('Title')
ax.set_ylabel('Y label')
ax.set_xlabel('X_label')
#Legands

axp = fig.add_axes([0,0,1,1])
axp.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')
axp.plot(y,x)
axp.legend(loc=0)

#-----------------------------------------------------------
#matplot part3
"""
plot appearance
"""
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='green')
ax.plot(x,y,color='#FF8C00',linewidth=3.9 , alpha = 0.5,linestyle = '--',marker='o', markersize = 10, 
        markerfacecolor="yellow",markeredgewidth=3,
        markeredgecolor='green' ) #RGB HEX Code











 







