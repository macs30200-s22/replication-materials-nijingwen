#!/usr/bin/env python
# coding: utf-8

# In[283]:


import numpy as np
import pandas as pd
import imblearn
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
get_ipython().run_line_magic('matplotlib', 'inline')
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pylab
pylab.rcParams["figure.figsize"] = (5.0, 4.0)
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_classification
from imblearn.under_sampling import NearMiss
from matplotlib import pyplot
from sklearn import preprocessing
from numpy import where
import functools
from functools import reduce
import operator
import seaborn as sns


# In[284]:


path='MACS30200_data.csv'
df = pd.read_csv(path)


# In[285]:


df.head()


# In[286]:


df.isna().sum()


# In[287]:


plt.figure(figsize = (16,5))
dataplot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)


# In[288]:


df_select = df[[ "GDP", "CPI", "Employment", "Population", "Graduations_College", "Graduations_University", "First_industry"]]


# In[289]:


df_selecty = df[[ "Employment"]]


# In[290]:


df_selectx = df[["GDP", "CPI", "Population", "Graduations_College", "Graduations_University", "First_industry"]]
df_selectx


# In[291]:


# data scaling
scaler = preprocessing.StandardScaler().fit(df_selectx)


# In[292]:


df_scaledx = scaler.transform(df_selectx)
df_scaledx


# In[293]:


df_selectx["GDP"] = df_scaledx[:,0]
df_selectx["CPI"] = df_scaledx[:,1]
df_selectx["Population"] = df_scaledx[:,2]
df_selectx["Graduations_College"] = df_scaledx[:,3]
df_selectx["Graduations_University"] = df_scaledx[:,4]
df_selectx["First_industry"] = df_scaledx[:,5]


# In[294]:


df_selectx


# In[295]:


X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(df_selectx, df_selecty, test_size = 0.2, random_state = 42)


# In[296]:


Linear_reg = LinearRegression()
model = Linear_reg.fit(X_train_reg, y_train_reg)

print(Linear_reg.score(X_train_reg, y_train_reg))
print(Linear_reg.score(X_test_reg, y_test_reg))


# In[297]:


coef_order = model.coef_[0].argsort()[::-1] #get the order of indices of reg.coef_
x, y = [], []
for i in zip(model.coef_[0][coef_order], model.feature_names_in_[coef_order]):
    y.append(i[0])
    x.append(i[1])
    print('{:.3f}'.format(i[0]), i[1])


# In[298]:


plt.figure(figsize = (16,5))
plt.bar(x, y)
plt.title("Feature Importance")


# In[299]:


#predict employment based on data in 2020
path2020='2020data.csv'
df_2020 = pd.read_csv(path2020)


# In[300]:


df_2020


# In[301]:


#scale
df_select2020 = df_2020[["GDP", "CPI", "Population", "Graduations_College", "Graduations_University", "First_industry"]]


# In[302]:


scaler_2020 = preprocessing.StandardScaler().fit(df_select2020)


# In[303]:


df_scaled2020 = scaler.transform(df_select2020)
#df_scaled2020


# In[304]:


df_select2020["GDP"] = df_scaled2020[:,0]
df_select2020["CPI"] = df_scaled2020[:,1]
df_select2020["Population"] = df_scaled2020[:,2]
df_select2020["Graduations_College"] = df_scaled2020[:,3]
df_select2020["First_industry"] = df_scaled2020[:,5]
df_select2020


# In[305]:


predict = model.predict(df_select2020)
#predict


# In[306]:


df_employ =  df_2020[["Province", "Employment"]]
#df_employ


# In[307]:


keys = df_employ['Province'].values.tolist()
#keys


# In[309]:


employ_num = df_employ.values[:,1:]
#employ_num


# In[310]:


gap = abs(employ_num - predict)
#gap


# In[311]:


gap_values = gap.tolist()
#gap_values


# In[312]:


gap_List_flat = functools.reduce(operator.iconcat, gap_values, [])
#gap_List_flat


# In[313]:


dictionary = dict(zip(keys, gap_List_flat))
#print(dictionary)


# In[314]:


df_gap = pd.DataFrame(dictionary.items(), columns=['Province', 'gap_value'])
#df_gap


# In[315]:


x = df_gap["Province"]
y = df_gap["gap_value"]


# In[316]:


plt.figure(figsize = (40,20))
plt.bar(x, y)
plt.title("gap between predicted employment and true employment in 2020")


# In[317]:


#14 province: Jiangsu
df_gap["gap_value"].max()


# In[282]:


#24 province: Xizang
df_gap["gap_value"].min()


# In[ ]:





# In[106]:


# relation between GDP and Employment
linear_GDP = sns.regplot(x="GDP", y="Employment", data=df_select)
linear_GDP.set_title("GDP and Employment")


# In[71]:


# relation between CPI and Employment
linear_CPI = sns.regplot(x="CPI", y="Employment", data=df_select)
linear_CPI.set_title("CPI and Employment")


# In[ ]:




