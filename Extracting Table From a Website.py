#!/usr/bin/env python
# coding: utf-8

# # Extracting table as website

# In[13]:


import pandas as pd


# In[5]:


url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'


# In[6]:


#here pandas is reading our URL of website
html = pd.read_html(url)


# In[14]:


#here is a table, but we need just one table, the list of states of brazil
html


# In[9]:


#So here we put parameter for pandas understading wich table I want. I use "match" for identify
html = pd.read_html(url, match='Unidade federativa')
html


# In[15]:


#Transforming our table in dataset
estados = html[0]


# In[16]:


estados


# In[ ]:




