#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import ploty.express as px
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv('us_perm_visas.csv')
df


# In[ ]:


df.head()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.tail()


# In[8]:


df.sample(1)


# In[11]:


df.columns.values


# In[16]:


df.case_no.nunique()


# In[19]:


df['case_number'].nunique()


# In[18]:


df.shape


# In[20]:


134990+238418


# In[25]:


df["case_number"]


# In[26]:


df["case_no"]


# In[29]:


casenoindex=df.columns.get_loc('case_no')
casenumberindex=df.columns.get_loc('case_number')
casenumberlist=[]
for value in df.iloc[0:135269,casenoindex]:
    casenumberlist.append(value)
    
for value in df.iloc[135269:374362,casenumberindex]:
    casenumberlist.append(value)
    
df["casenumber"]=casenumberlist


# In[30]:


df.columns


# In[31]:


df.drop(['case_no','case_number'],axis=1,inplace=True)


# In[32]:


df.columns


# In[33]:


df["case_status"].unique()


# In[16]:


for value in df.case_status.unique():
    print(len(df[df["case_status"]==value]), "occurence of status '{}'".format(value))
    


# In[14]:


df.loc[df.case_status=="Certified_Expired","case_status"]="Certified"


# In[15]:


df.case_status.value_counts()


# In[7]:


df=df[df.case_status!="Withdrawn"]


# In[8]:


df


# In[23]:


df.shape


# In[25]:


df[df.case_status=="Certified_Expired"]


# In[13]:


df.loc[df.case_status=="Certified_Expired", "case_status"]="Certified"
df.case_status.value_counts(normalize=True)*100


# In[ ]:


#  only 7.2% application denied


# In[14]:


df.shape


# In[15]:


df.dropna(axis=1,how="all",inplace=True)
df.dropna(axis=0,how="all",inplace=True)


# In[16]:


df.shape


# In[17]:


df.columns


# In[19]:


for column in df.columns:
    print(f"the missing value for {column} is {df[column].isnull().sum()}")


# In[20]:


df["decision_date"]


# In[27]:


df["decision_date"]=pd.to_datetime(df["decision_date"])


# In[28]:


df['decision_date'].dtypes


# In[ ]:


# year wise visa status


# In[31]:


df["year"]=df["decision_date"].dt.year


# In[32]:


df["year"]


# In[33]:


sns.countplot(x="year",hue="case_status",data=df)


# In[ ]:


# there is upward trend in both 


# In[35]:


df["employer_city"].value_counts()


# In[52]:


df["employer_city"]=df["employer_city"].str.upper()


# In[53]:


df["employer_city"].value_counts()


# In[57]:


sns.countplot(x="employer_city",hue="year",data=df,order=df.employer_city.value_counts()[:10])


# In[ ]:


# top 10 employer for visa application


# In[61]:


top_empl=df["employer_name"].value_counts().head(10)


# In[63]:


top_empl.plot(kind="bar",color="red")
for i,v in enumerate(top_empl):
    plt.text(i,v+10,str(v),ha="center",va="bottom",fontsize=10)


# In[64]:


df["us_economic_sector"]


# In[ ]:


us economis_counts={}
   for value in df["us_economic_sector"].drop()na:
        if value 
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




