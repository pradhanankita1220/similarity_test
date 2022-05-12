#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[30]:


def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)


# In[37]:


link="https://docs.google.com/spreadsheets/d/1vqu1xS_5STc_AD3eiZBCwao9lEBkzyj2c-vkBd6IsAk/export?format=csv&gid=1590792044"

df=pd.read_csv(link)
df.head(5)


# In[38]:


len(df)


# In[ ]:





# In[45]:


for i in range(0,100):
    text1= df["text1"][i]
    text2= df["text2"][i]
    sentences = [text1,text2]
    sentences = [sent.lower().split(" ") for sent in sentences]
    df["similarity score"][i]=jaccard_similarity(sentences[0], sentences[1])


# In[48]:


df.head(20)


# In[ ]:





# In[ ]:




