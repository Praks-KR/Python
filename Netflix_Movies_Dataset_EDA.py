#!/usr/bin/env python
# coding: utf-8

# # Netflix Movies - EDA

# In[1]:


# Netflix Movies

# Data Preparation and cleaning
## Loading data using Pandas
## Analyse data and columns
## Dealing with the missing values



# ## Importing neccessary libraries and loading Data
# 

# In[93]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


df = pd.read_csv('D://Python/netflix_titles.csv')


# In[11]:


df.columns


# In[13]:



df


# In[15]:


df.describe()


# In[16]:


df.info()


# ## Data Preparation and Cleaning
# 
# ### Missing Values

# In[19]:


#missing values
missing = df.isna().sum().sort_values(ascending = False)

#2.3k director names are missing


# In[20]:


missing_per = missing/len(df)


# In[21]:


missing_per


# In[22]:


len(df)


# In[24]:


missing_per[missing_per !=0]


# ### Dropping 'director' field as it as its 30% values are missing.

# In[59]:



df= df.drop(['director'], axis = 1)


# In[62]:


df.head()
df.isna().sum().sort_values(ascending = False)


# ### Filling missing values in 'cast' field with "unknown"

# In[64]:



df.cast.fillna("unknown", inplace = True)


# In[65]:


df.cast.isna().sum()


# ### Filling missing values in 'country' field as "NA"

# In[71]:



df.country.fillna("NA", inplace = True)


# In[67]:


df.isna().sum().sort_values(ascending = False)


# In[74]:


df.rating.value_counts()


# In[75]:


#most the values in rating field is "TV-MA", using this value to fill missing values.
df.rating.fillna("TV-MA", inplace = True)


# In[76]:


df.isna().sum().sort_values(ascending = False)


# In[77]:


df.date_added.value_counts()


# ### most the values in date_added field is "January 1 , 2020". using this value to fill missing values.

# In[78]:



df.date_added.fillna("January 1 , 2020", inplace = True)


# In[79]:


df.isna().sum().sort_values(ascending = False)


# ## Exploratory Data Analysis and Visualization
# ### Columns to Analyse:
# #### 1. Type
# #### 2. Country
# #### 3. Rating

# In[80]:


df.type.value_counts()


# In[82]:


df.columns


# In[83]:


df.country.value_counts()


# In[89]:


#replacing "unknown" values in country field to "united states"
df['country'].replace(to_replace = "unknown", value = "United States", inplace = True)


# In[95]:


countries = df.country.value_counts().head(10)   #top 10 countries


# In[96]:


plt.figure(figsize=(10,10))
ax=sns.barplot(countries.values, countries.index)
ax.set_xlabel("Number of Content")
ax.set_ylabel("Number of Country")


# In[ ]:


#United states and India are the top contributors


# In[121]:


x= df.rating.value_counts()
x


# In[130]:


plt.figure(figsize=(10,10))
ax=sns.barplot(x.index, x.values).set(title='Count vs Rating')


# In[ ]:


#TV-MA is highly watched followed by TV-14 and TV-PG.


# In[137]:


y = df.type.value_counts()
y


# In[141]:


plt.figure(figsize=(10,10))
plt.pie(y.values,labels=["Movies","TV Shows"],autopct="%1.1f%%")
plt.legend(title = 'Type')
plt.show()


# In[145]:



z= df.release_year.value_counts().head(20)
z


# In[147]:


plt.figure(figsize=(10,10))
ax = sns.barplot(z.index, z.values).set_title('Release Year')



# In[ ]:


#Most of Netflix contents are released in the year of 2018,2017,2019,2016 and 2020 respectively. 


# In[160]:


a


# In[178]:


# Splitting year from date_added field to create new column.
df["year"]= df.date_added.apply(lambda x: str(x).split(",")[-1]).sort_values(ascending = False)


# In[ ]:





# In[207]:


a= df.year.value_counts().head(10)


# In[208]:


#contents added to netflix over the years
plt.figure(figsize = (10,10))
ax= sns.barplot(a.index, a.values)


# In[ ]:


#Highest number of contents added in 2019, 2020 and 2018 respectively.


# In[211]:


plt.figure(figsize= (10,10))
sns.countplot(x = 'rating', hue='type', data = df)
Plt.show()


# In[212]:


plt.figure(figsize= (10,10))
sns.countplot(x = 'type', hue='type', data = df)
Plt.show()


# In[209]:


df.info()


# In[210]:


df


# In[ ]:





# In[50]:


type(date_added)


# In[51]:


df.date_added[0]


# In[53]:


type(df.release_year)


# In[ ]:


titl


# In[54]:


df.info()


# ## Summary and Conclusion:
# ### 1. United states and India are the top contributors
# ### 2. TV-MA is highly watched followed by TV-14 and TV-PG.
# ### 3. Most of Netflix contents are released in the year of 2018,2017,2019,2016 and 2020 respectively.
# ### 4. Highest number of contents added in 2019, 2020 and 2018 respectively.

# In[ ]:




