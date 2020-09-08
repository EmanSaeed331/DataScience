#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""

#introduction to seaborn

"""
@https://seaborn.pydata.org/
- Seaborn is a statical plotting library.
- it has a beutiful default style.
- it also is desined to work very well with pandas datafram objects.
"""
#installing
"""
- we can install it by :
    1-conda install seaborn.
    2-pip install seaborn.
"""
"""
- Distribution Plots  
- we will create a dataframe called tips 
- tips is a data set, tips is consists of 7 columns and this is basically refering to peaple who has a meal
  and left a tip  .
- distplot -> it show a histogram and what is know K D E kerel denisty estimation.
- we can remove the line of K D E  by adding additional argument -> kde = false.
- it finally show the histogram without the K D E .
- in a histogram the y-axis you have a count and then you have these bars on X-axes as bins .
- we use a number of bins as and arguments 
"""
import seaborn as sns
import numpy as np
import matplotlib as plt
tips = sns.load_dataset('tips')
tips.head()
print(tips.head())
sns.distplot(tips['total_bill'],kde=False , bins = 100)
#JoinPlots
"""
- JoinPlots allows you to basically match up to this plots for by various data meaning 
  you can essentially combine tow diffrent distribution plots.
-  x , y is a column names
- it show two distribution plot .
- kind make you use any kind of distrivution like hex .
- kind may be reg -> it will make a linear regression plot , 
  it just showing almost like linear fit to the scattered point data .
-kde is a default kind 
"""
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')

#pairplot
"""
- pairplot is essentially going to plot pairwise relationships across 
  an entire data frame at least for the numerical columns. 
-pairplot has multiple arguments : 
    1- data to plot.
    2- hue -> the column name of categorical means not numerical or continous but actual categories.
    3- pallet -> is used actually to color this.
"""
sns.pairplot(tips)

sns.pairplot(tips,hue='sex',palette='coolwarm')

#rugplot
"""
- rugplot: is just like a distribution plot we can pass a single column here.

"""
#sns.rugplot(tips['total_bill'],kde=False)
#-----------------------------------------------------------------------
#categorical plots .
"""
- categorical plot is a general plots that is used to aggreagte 
  the categorical data based off some function and by default that;s the mean you can almost think.
- estimator is a function that ia  ans aggregate function .
- we can use a standred deviation 
"""

tips.head()
sns.barplot(x='sex',y='total_bill',data=tips,estimator = np.std)



#countPlot
"""
- countplot : in seaborn is essentially the same as bar plot expect the estimator 
  is explicity counting the number of occurences, 
  and becouse of that we only set the x value and then we sit in the data equals tips.
"""
sns.countplot(x='sex',data=tips)

#Box plots and violent plots.
"""
- this type of plots are used to show that distribution of categorical data.
- box plot is also known as box and whisker plot.
- box plot is showing the core tiles of the data set .
- violent plots is a very similar role to a box plot.
"""
 
sns.boxplot(x='day',y='total_bill',data=tips)

sns.violinplot(x='day',y='total_bill',data=tips, hue='sex',split=True)

#strip plot 
"""
- strip plot is going to draw a scatterplot where one variable is categorical .
- one issue in this strip plot that you can't really tell how many points are stacked on top of each other 

"""
sns.stripplot(x='day',y='total_bill',data=tips,jitter =True,hue='sex')

#swarm plot
"""
- swarmplot is very similar tp strip plot except the points are adjusted so theat they don't overlap

"""
sns.swarmplot(x='day',y = 'total_bill',data=tips)
sns.swarmplot(x='day',y = 'total_bill',data=tips , color='black')

#Factor plot
"""
- factor plot is actually just the most general form all these plots 
"""
#sns.factorplot(x='day',y='total_bill',data=tips,kind='bar',kind='violin')

#----------------------------------------------------------
#Matrix plots.

tips2 =sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips2.head()

tips2.corr()

tc = tips.corr()
sns.heatmap(tc)
sns.heatmap(tc,annot=True,cmap='coolwarm')
flights.pivot_table(index='month',columns='year',values='passengers')

fp = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fp)
sns.clustermap(fp)

#---------------------------------------------------- 
#Grids 
iris = sns.load_dataset('iris')
iris.head()
sns.PairGrid(iris) 
g = sns.PairGrid(iris)
#g.map_diag(sns.displot)
#g.map_upper(plt.scatter)
#g.map_lowe(sns.kdeplot)

#g = sns.FacetGrid(data=tips,col = 'time',row='smoker')

#g.map(sns.displot,'total_bill')
#------------------------------------------------------------
#Regression Plots 

"""
regression plot dependen greatly on machine leaning splittiing the fit line.
"""
tips = sns.load_dataset('tips')
tips.head()
sns.lmplot(x='total_bill',y='tip',data=tips,hue = 'sex',markers = ['o','v'])

sns.lmplot(x ='total_bill',y='tip',data=tips,col = 'day',hue='sex')





