#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""

import numpy as np
import pandas as pd
import seaborn as sns

"""
df1 = pd.read_csv('df1',index_col=0)

df1.head()
df2 = pd.read_csv('df2')
df2.head()
df1['A']
df1['A'].hist(bins=30)
df1['A'].plot(kind='hist')
df2.plot.area(alpha=0.4)
df2.plot.bar(stacked=True)
df1.plot.line()
df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)
df1.plot.scatter(x='A',y='B')
df1.head()
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')
"""
#-------------------------------------------------------------------
#Plotly and Cufflinks 

"""
@https://plotly.com/
- it is allows you to create interactive visualizations 
- plotly is an interactive visualization library.
- Cufflinks connects plotly with pandas .
- plotly is a compatable with a variety of tools such as our Matlab m execel and JavaScript.
- cufflinks is a library  connects plot with pandas .


"""
#installing
"""
- we can install them by :
    1-pip install plotly.
    2-pip install cufflinks.
"""
"""
- from plotly import __version__ to showing us the version of plottly.
- from plotly.offline import download_plotlyjs -> to import offline libraries.
- we can use an interactive javascript library.
 
"""
import pandas as pd
import numpy as np
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs ,init_notebook_mode ,plot,iplot
print(__version__)
init_notebook_mode(connected=True )
cf.go_offline()

#Createing a data 
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df)
print(df.head())

# - we make a dataframe as a dictionary.

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2)


df.plot()
df.iplot()
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=20)


df2.iplot(kind='bar',x='Category',y='Values')
df.iplot(kind='box')

df3 = pd.DataFrame({'X':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[500,400,300,200,100]})

print(df3)

df3.iplot(kind='surface')


df.iplot(kind='bubble',x='A',y='B',size='C')

df.scatter_matrix()

#-------------------------------------
#- geographical plotting 
"""
- geographical plotting is usually challenging to due the various formats the data can come in.
- we will use plotly for plotting .
- we will use Matplotlib also has a basemap extension.

"""

#Choropleth Maps
"""
- 

"""
#import plotly.plotly as py -> Deprecated
import chart_studio.plotly as py
import plotly.graph_objs as go

data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale = 'Potland',
            text= ['text 1','text 2','text 3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title Goes Her'})

layout = dict(geo={'scope':'usa'})
go.Figure(data = [data],layout=layout)
choromap = go.Figure(data = [data],layout=layout)
iplot(choromap)

df = pd.read_csv('2014_world_GDP')
df.head()

data = dict(type ='choropleth',
            locations = df['CODE'],
            z = df['GDP (BILLIONS)'],
            text = df['COUNTRY'],
            colorbar = {'title':'GDP in Billions USD'}
            )

layout = dict(title = '2014 Global GDP',
              geo = dict  (showframe = False,
                            projection = {'type':'Mecator'}))

choromap3 = go.Figure(data=[data],layout=layout)

iplot(choromap3)












