#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv(r"C:\Users\Swastic\Desktop\INeuron\Datasets\Dataset\data1\cleaned_travel.csv")
data.head() #this helps in looking at the data kind of introduction to the data


# In[3]:


data.tail() #this helps in looking at the bottom of data 


# In[5]:


data.shape #how many rows and columns are there in the data


# In[6]:


data.info() #helps in getting the information whether there is any null value, how many values are there, is it matching with the number of rows and data type


# In[7]:


data.columns #all columns names in the data


# In[8]:


cat_col = [fea for fea in data.columns if data[fea].dtype == 'O']


# In[9]:


num_col = [fea for fea in data.columns if data[fea].dtype != 'O']


# In[11]:


data[cat_col]


# In[12]:


data.memory_usage()


# # Missing Values

# In[13]:


data.isnull().sum() #cheking for the null values
#conclusion:there are no null values in the data


# In[15]:


data.duplicated() #checking for the duplicate values in data
#conclusion: there are no duplicate values in the data


# In[17]:


data.nunique() #checking for unique values in the data
# Conclusion: Below are the number of unique values in each columns in the data


# In[20]:


data.describe().T #checking for the statistical description of the numerical data
# Conclusions: We can see from below description column wise, the mean of product taken is 0.18 and it has a range from 0 to 1 that means more people have opted out than taking the product. Similarly, average age of the data set is 37.5 years and people have preferred higher star rating of the properties.


# In[21]:


data.corr() #checking for data correlations between columns
# Conslusion: With the increase in age duration of pitch decreases, either people grow more impaitent with age or they just decline the pitch.Also, with the increase in duration of the pitch number of person visiting is increasing which means duration of pitch has positive effect on people.With the increase in age number of trips also increases.


# In[22]:


data.skew() #checking for the skewness in data
# Conclusion: Monthly income is skewed on the right side leading to the conclusion that people earning more goes for vacations.


# In[23]:


sns.distplot(data['MonthlyIncome']) #cheking for skewness of the monthly income with dist plot


# In[30]:


#checking for p-value(for normal distribution p-value > 0.05)
from scipy.stats import normaltest
data_num = data[num_col]
for col in data_num.columns:
    x = normaltest(data_num[col])[1]*100
    print(x)
#Conclusion: All the given data has a p-value lesser than 0.05, that means we have no data which is distributed normally.


# In[31]:


#Dist plot of all the data
num_col


# In[32]:


sns.distplot(data_num['ProdTaken'])


# In[33]:


sns.distplot(data_num['Age'])


# In[34]:


sns.distplot(data_num['CityTier'])


# In[35]:


sns.distplot(data_num['DurationOfPitch'])


# In[36]:


sns.distplot(data_num['NumberOfPersonVisiting'])


# In[37]:


sns.distplot(data_num['NumberOfFollowups'])


# In[38]:


sns.distplot(data_num['PreferredPropertyStar'])


# In[39]:


sns.distplot(data_num['NumberOfTrips'])


# In[40]:


sns.distplot(data_num['Passport'])


# In[41]:


sns.distplot(data_num['PitchSatisfactionScore'])


# In[42]:


sns.distplot(data_num['OwnCar'])


# In[43]:


sns.distplot(data_num['NumberOfChildrenVisiting'])


# In[44]:


sns.distplot(data_num['MonthlyIncome'])


# In[45]:


#Conclusion: Except Age, Duration of pitch and monthly income all other columns are discrete


# In[76]:


numeric_col = ['Age','DurationOfPitch','MonthlyIncome']
numeric_col_data = data[numeric_col]
numeric_col_data


# In[ ]:




