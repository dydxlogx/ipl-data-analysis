#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[5]:


ipl=pd.read_csv('matches.csv')


# In[6]:


ipl.head()


# In[7]:


ipl.shape


# In[8]:


ipl['player_of_match'].value_counts()


# In[9]:


ipl['player_of_match'].value_counts()[0:10]


# In[10]:


ipl['player_of_match'].value_counts()[0:5]


# In[11]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[13]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[15]:


ipl['result'].value_counts()


# In[16]:


ipl['toss_winner'].value_counts()


# In[25]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[26]:


batting_first.head()


# In[28]:


plt.figure(figsize=(5,5))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.show()


# In[29]:


batting_first['winner'].value_counts()


# In[30]:


plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[34]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.if%%')
plt.show()


# In[35]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[36]:


batting_second.head()


# In[37]:


plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[38]:


batting_second['winner'].value_counts()


# In[41]:


plt.figure(figsize=(5,5))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["purple","blue","red"])
plt.show()


# In[43]:


plt.figure(figsize=(5,5))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[44]:


ipl['season'].value_counts()


# In[45]:


ipl['city'].value_counts()


# In[ ]:


# import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[ ]:




