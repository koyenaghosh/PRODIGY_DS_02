#!/usr/bin/env python
# coding: utf-8

# # Perform data cleaning and exploratory data analysis (EDA) on a dataset of your choice, such as the Titanic dataset from Kaggle. Explore the relationships between variables and identify patterns and trends in the data.

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


titanic = pd.read_csv('titanic.csv')
pd.set_option('display.max_rows',None)


# In[4]:


titanic.drop(columns=['cabin','name','ticket','boat','body','home.dest'],inplace=True)


# In[5]:


titanic.head()


# In[7]:


titanic.loc[:,['age','sibsp','parch','fare']].hist(bins=20,figsize=(10,10))
plt.show()


# In[9]:


sns.catplot(data=titanic,kind='bar',x='sex',y='parch',hue='survived')
plt.show()


# In[14]:


sns.catplot(data=titanic,kind='bar',x='sex',y='sibsp',hue='survived')
plt.show()

