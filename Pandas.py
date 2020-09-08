#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:19:32 2020

@author: eman-saeed
"""
#introduction to pandas 
"""
Pandas is an open source library built on top of numpy.
it allows for fast analysis and data cleaning and preparation.
it excels in performance and productivity.
it has built-in visualization features.

"""
#installing of pandas 
"""
you can install pandas by: 
    1-conda install pandas .
    2-pip install pandas .
"""
#Section Overview 
"""
-Series .
-DataFrames.
-Missing Data.
-GroupBy.
-Merginig, Joining , and Concatenating.
-Operations.
-Data input and Output.
"""
#Series 
"""
series is the first main data type that will be working 
with pandas and that build off of Cares to work with data frames .
we will have a labeled index series .

find index of the String -> series['']
"""

import numpy as np 
import pandas as pd 

labels  = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(data = my_data))


pd.Series(arr,labels)

print(pd.Series(data=[sum,print,len]))

ser1 = pd.Series([1,2,3,4],['EGYPT','Germany','USSR','Japana'])
print(ser1)

ser2 = pd.Series([1,2,5,3],['Egypt','Germany','Italy','Japan'])

print(ser1['EGYPT'])


ser3 = pd.Series(data=labels)
print(ser3)

#-------------------------------------------------
#Data frame 
"""
data frame is a main tool when working with pandas
seeds mean : is just to make sure that we get the same random numbers.

-to generate a data fram , with a random matrix by randn labeled with A, B ,C, D
-to print a specific column -> df['W']
-to show type of -> type(df['W'])

"""
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['W'])
print(type(df['W']))

print(df['X'])
#--------------------------------------------------------
#Data Frame part2 
#conditional selection 

"""
a very important feature of pandas is the ability to perform conditional 
selection using bracket notation and it will be a very similar to numpy.
1- df > 0 -> where the data frame greater than zero
2-when we print -? NaN it is to be false value
we can apply a multiple conditional selection in multiple list

"""
print(df>0)

booldf=df>0
print(booldf)
print(df['W']>0)
df[df['W']>0]


print(df[df['W']>0]['X'])
boolser  = df['W']>0
myColumns = ['Y','X']
result = df[boolser]
result [myColumns]
print(result)


"""
the concept of using multiple conditions 
such as two or more conditions :
    we can use multiple condtions by the built in operators (and),(or) , or by a operator symbols (&),(|)
                                         
we can reset the index of data by df.reset_index() 
"""
print(df[df['W']>0 & (df['Y'] > 1 )])

print(df.reset_index())

newIndex = 'CA NY WY OR CO'.split()
print(newIndex 
      )

df['State'] = newIndex
print(df)

df.set_index('State')

print(df)
#---------------------------------------------------------
#data frame part3
"""
we are going to learn about multi index and index higher key.
ZIP function : is make a pairs of tuples .
there is a special function from pandas 
df.loc -> that will show the data with G1
"""
outside = ['G1','G1','G1','G2','G2','G2']
inside  =[1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(outside)
print(inside)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)
print(df.loc['G1'])
print(df.index.names)

df.index.names = ['Groups','Num']
df.loc['G2'].loc[2]['B']
print(df.xs('G1'))
print(df.xs(1,level='Num'))
#-----------------------------------------------------------
#Missing Data
"""
hint : we can creat a data frame from a dictionary.
-np.nan is a missing value.
-dropna -> is going to drop any row with any single or water more or missing values .
"""
d={'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,5,6,]}
df1 = pd.DataFrame(d)
print(df1)
print(df1.dropna())

print(df1)
df['A']

df['A'].fillna(value=df['A'].mean())

#---------------------------------------------------------------
#Groupby
"""
-groupby allows you to group together rows based off a column and then perform
some sort of aggregate function on them.
-we make a group by id coloumn and aggregate them in sort function

"""
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}


df2 = pd.DataFrame(data)
print(df2)
print(df2.groupby('Company'))
df2.groupby('Company') #->it will show goupby in memory so we have to store this as a variable
gby = df2.groupby('Company')
print(gby.mean())

print(gby.std())


df2.groupby('Company').sum().loc['FB']


print(df2.groupby('Company').describe())

print(df2.groupby('Company').describe().transpose())
#-----------------------------------------------------------------
#Merging Joining and Concatenating 

"""
in this lecture we will learn how to combine data frames throoough
a variety of methods instead of actually life 
#Concatenating

"""
dafram = pd.DataFrame({
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
    index=[0,1,2,3])
dafram2 = pd.DataFrame({
                    'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
    index=[4,5,6,7])

dafram3 = pd.DataFrame({
                    'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
    index=[8,9,10,11])
print(dafram)
print(dafram2)
print(dafram3)

print(pd.concat([dafram,dafram2,dafram3]))
#the below line is bunch of missing values
print(pd.concat([dafram,dafram2,dafram3],axis=1))


#Marging 

leftDf = pd.DataFrame({'Key':['k0','k1','k2','k3'],
                       'A':['A0','A1','A2','A3'],
                       'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['k0','k1','k2','k3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})

print(leftDf)
print(right)


#print(pd.merge(leftDf,right,how='inner',on='key'))

#print(pd.merge(leftDf,right,how='outer',on=['key1','key2']))



#-----------------------------------------------------
#operations 
dfnew= pd.DataFrame({'col1':[1,2,3,4],
                     'col2':[444,555,666,444],
                     'col3':['abc','def','ghi','xyz']})

"""
unique method will return the unique values in colomn instead of actially
wanting the array of unique values.
2- df['col2'].value_counts() ->it retuen the count of repeated numbers.
"""
            
print(df.head())
print(dfnew['col2'].unique())
print(dfnew['col2'].nunique())
print(dfnew['col2'].value_counts)

print(dfnew) 
print(dfnew['col1']>2) 

print(dfnew[(dfnew['col1']>2) & (dfnew['col2']==444)])

print(dfnew['col1']>2)

def times(x):
    return x*3
s = times(10)
print(s)

"""
we apply the function (times ) it will mulitply each single element 
by 3 in the col1
2-we use lambda expression to apply times function in each single elemnt.
3-dfnew.index is showinf a columns with the index of them.
4-dfnew.sort_value -> it sorts Rows of col2 from the smaller to greater.
5-dfnew.isnull -> check if there is any null data.
6-we can use a DFT pivot table-> is just creat a multi index out of this table or a data frame
the method to do this : pivor_table
"""
print(dfnew['col1'].apply(times))
print(dfnew['col2'].apply(lambda x:x*2))

print(dfnew.columns)
print(dfnew.index)
print(dfnew.sort_values('col2'))

print(dfnew.isnull())

data1= {'A':['foo','foo','foo','bar','bar','bar','bar'],
        'B':['one','one','two','two','one','three','three'],
        'C':['x','y','x','x','y','x','y'],
        'D':[1,2,3,2,5,4,9]}
dfnew2 = pd.DataFrame(data1)
print(dfnew2)

print(dfnew2.pivot_table(values='D',index=['A','B'],columns=['C']))
#----------------------------------------------------
#Data input and output
"""
pandas is a library that has the ability to read and write a data.
-the sources for reading a data is :
    1-CSV.
    2-Excel.
    3-HTML.
    4-SQL.
""" 
"""
in order to work with Html files  and sql database with pandas 
we have to install the following libraries:
    1-conda install sqlalchemy.
    2-conda install lxml
    3-conda install html5lib.
    4-conda install BeutifulSoup4.
"""
#pd.read_csv('example.csv')

#df = pd.read_csv('example.csv')
#df.to_csv('My_output')
#pd.read_csv('My_output')

htdata =pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print(htdata)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')

print(df.to_sql('my_table',engine))









 