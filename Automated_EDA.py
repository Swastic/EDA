#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pandas-profiling


# In[4]:


#importing required packages
import pandas as pd
import pandas_profiling
import numpy as np

#importing the data
df = pd.read_csv(r'C:\Users\Swastic\Desktop\INeuron\Datasets\Dataset\data1\cleaned_travel.csv')

#descriptive statistics
pandas_profiling.ProfileReport(df)


# In[5]:


pip install sweetviz


# In[7]:


import sweetviz
import pandas as pd
df = pd.read_csv(r'C:\Users\Swastic\Desktop\INeuron\Datasets\Dataset\data1\cleaned_travel.csv')
df.head()


# In[8]:


my_report  = sweetviz.analyze([df,'Train'], target_feat='MonthlyIncome')
my_report.show_html('FinalReport.html')


# In[9]:


pip install autoviz


# In[10]:


from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
df = AV.AutoViz(r'C:\Users\Swastic\Desktop\INeuron\Datasets\Dataset\data1\cleaned_travel.csv')


# In[ ]:




