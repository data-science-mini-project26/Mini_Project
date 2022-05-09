#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
a = pd.read_csv("s3://project-b-data/1.csv")


# In[2]:


a


# In[2]:


b = pd.read_csv("s3://project-b-data/2.csv")


# In[4]:


b


# In[3]:


c = pd.read_csv("s3://project-b-data/3.csv")


# In[8]:


c


# In[4]:


d = pd.read_csv("s3://project-b-data/4.csv")


# In[11]:


d


# In[5]:


e = pd.read_csv("s3://project-b-data/5.csv")


# In[13]:


e


# In[6]:


f=pd.read_csv("s3://project-b-data/6.csv")


# In[15]:


f


# In[7]:


g=pd.read_csv("s3://project-b-data/7.csv")


# In[18]:


g


# In[8]:


h=pd.read_csv("s3://project-b-data/8.csv")


# In[20]:


h


# In[9]:


z =[a,b,c,d,e,f,g,h]


# In[10]:


z = pd.concat(z)


# In[11]:


z


# In[12]:


z.to_csv(f"s3://project-b-data/b02.csv",index = False)


# In[ ]:


aa=pd.read_csv("s3://project-b-data/11.csv")


# In[ ]:


aa


# In[ ]:


bb=pd.read_csv("s3://project-b-data/22.csv")

