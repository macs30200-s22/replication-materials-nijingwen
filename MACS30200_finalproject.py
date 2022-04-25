#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
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


# In[80]:


path='MACS30200_data.csv'
df = pd.read_csv(path)


# In[81]:


df.head()


# In[82]:


df.isna().sum()


# In[83]:


plt.figure(figsize = (16,5))
dataplot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)


# In[84]:


df_select = df[[ "GDP", "CPI", "unemployment_rate", "Population", "Graduations_College", "Graduations_University", "First_industry"]]


# In[85]:


df_selecty = df[[ "unemployment_rate"]]


# In[86]:


df_selectx = df[["GDP", "CPI", "Population", "Graduations_College", "Graduations_University", "First_industry"]]
df_selectx


# In[87]:


# data scaling
scaler = preprocessing.StandardScaler().fit(df_selectx)


# In[88]:


df_scaledx = scaler.transform(df_selectx)
df_scaledx


# In[89]:


df_selectx["GDP"] = df_scaledx[:,0]
df_selectx["CPI"] = df_scaledx[:,1]
df_selectx["Population"] = df_scaledx[:,2]
df_selectx["Graduations_College"] = df_scaledx[:,3]
df_selectx["Graduations_University"] = df_scaledx[:,4]
df_selectx["First_industry"] = df_scaledx[:,5]


# In[90]:


df_selectx


# In[91]:


X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(df_selectx, df_selecty, test_size = 0.2, random_state = 42)


# In[92]:


Linear_reg = LinearRegression()
model = Linear_reg.fit(X_train_reg, y_train_reg)

print(Linear_reg.score(X_train_reg, y_train_reg))
print(Linear_reg.score(X_test_reg, y_test_reg))


# In[93]:


coef_order = model.coef_[0].argsort()[::-1] #get the order of indices of reg.coef_
x, y = [], []
for i in zip(model.coef_[0][coef_order], model.feature_names_in_[coef_order]):
    y.append(i[0])
    x.append(i[1])
    print('{:.3f}'.format(i[0]), i[1])


# In[94]:


plt.figure(figsize = (16,5))
plt.bar(x, y)
plt.title("Feature Importance")


# In[95]:


#predict employment based on data in 2020
path2020='2020data.csv'
df_2020 = pd.read_csv(path2020)


# In[96]:


df_2020


# In[97]:


#scale
df_select2020 = df_2020[["GDP", "CPI", "Population", "Graduations_College", "Graduations_University", "First_industry"]]


# In[98]:


scaler_2020 = preprocessing.StandardScaler().fit(df_select2020)


# In[99]:


df_scaled2020 = scaler.transform(df_select2020)
#df_scaled2020


# In[100]:


df_select2020["GDP"] = df_scaled2020[:,0]
df_select2020["CPI"] = df_scaled2020[:,1]
df_select2020["Population"] = df_scaled2020[:,2]
df_select2020["Graduations_College"] = df_scaled2020[:,3]
df_select2020["First_industry"] = df_scaled2020[:,5]
df_select2020


# In[101]:


predict = model.predict(df_select2020)
#predict


# In[102]:


df_employ =  df_2020[["Province", "unemployment_rate"]]
df_employ


# In[103]:


keys = df_employ['Province'].values.tolist()
#keys


# In[104]:


employ_num = df_employ.values[:,1:]
#employ_num


# In[105]:


gap = employ_num - predict
#gap


# In[106]:


gap_values = gap.tolist()
#gap_values


# In[107]:


gap_List_flat = functools.reduce(operator.iconcat, gap_values, [])
#gap_List_flat


# In[108]:


dictionary = dict(zip(keys, gap_List_flat))
#print(dictionary)


# In[109]:


df_gap = pd.DataFrame(dictionary.items(), columns=['Province', 'gap_value'])
df_gap


# In[203]:


df_gap.to_csv('gap.csv')


# In[204]:


coef_order1 = model_covid.coef_[0].argsort()[::-1] #get the order of indices of reg.coef_
x, y = [], []
for i in zip(model_covid.coef_[0][coef_order], model_covid.feature_names_in_[coef_order1]):
    y.append(i[0])
    x.append(i[1])
    print('{:.3f}'.format(i[0]), i[1])


# In[205]:


plt.figure(figsize = (40,20))
matplotlib.rcParams.update({'font.size': 30})
plt.bar(x, y)
plt.title("Feature importance of unemployment rate from 2008-2019", size = 30)


# In[206]:


x = df_gap["Province"]
y = df_gap["gap_value"]


# In[217]:


plt.figure(figsize = (80,25), dpi=100)
matplotlib.rcParams.update({'font.size': 25})
plt.bar(x, y)
plt.title("gap between predicted umemployment rate and true unemployment rate in 2020", size = 30)


# In[113]:


#14 province: Henan
abs(df_gap["gap_value"]).max()


# In[114]:


#24 province: Fujian
abs(df_gap["gap_value"]).min()


# In[115]:


df_2020.head()


# In[116]:


plt.figure(figsize = (16,5))
dataplot = sns.heatmap(df_2020.corr(), cmap="YlGnBu", annot=True)


# In[117]:


#scale
df_2020_scale = df_2020.drop(columns = "Province")
scaler = preprocessing.StandardScaler().fit(df_2020_scale)


# In[118]:


df_covid = scaler.transform(df_2020_scale)
#df_covid


# In[119]:


df_2020["GDP"] = df_covid[:,0]
df_2020["CPI"] = df_covid[:,1]
df_2020["Population"] = df_covid[:,2]
df_2020["Graduations_College"] = df_covid[:,3]
df_2020["Graduations_University"] = df_covid[:,4]
df_2020["First_industry"] = df_covid[:,5]
df_2020["Confirmed"] = df_covid[:,5]
df_2020["Death"] = df_covid[:,6]
df_2020["Recovery"] = df_covid[:,7]
df_2020["gap_value"] = df_covid[:,8]
df_2020


# In[122]:


#statistics
import statsmodels.api as sm
x = df_2020[['Confirmed', "Death", "Recovery"]]
y = df_2020[['gap_value']]
covid_data = sm.add_constant(x)
model_covid = sm.OLS(y, covid_data).fit()
summary_covid = model_covid.summary()
print(summary_covid)


# In[123]:


X_reg_covid = df_2020[["GDP", "CPI", "Population", "Graduations_College", "Graduations_University", "First_industry", "Confirmed", "Death", "Recovery"]]
y_reg_covid = df_2020[["unemployment_rate"]]


# In[124]:


Linear_reg = LinearRegression()
model_covid = Linear_reg.fit(X_reg_covid, y_reg_covid)


print(Linear_reg.score(X_reg_covid, y_reg_covid))


# In[125]:


# relation between GDP and gap_Emloyment
linear_GDP = sns.regplot(x="GDP", y="gap_value", data=df_2020)
linear_GDP.set_title("GDP and gap_Employment")


# In[126]:


# relation between CPI and gap_Employment
linear_CPI = sns.regplot(x="CPI", y="gap_value", data=df_2020)
linear_CPI.set_title("CPI and gap_Employment")


# In[127]:


# relation between Population and gap_Employment
linear_Population = sns.regplot(x="Population", y="gap_value", data=df_2020)
linear_Population.set_title("Population and gap_Employment")


# In[128]:


# relation between Graduations_College and gap_Employment
linear_College = sns.regplot(x="Graduations_College", y="gap_value", data=df_2020)
linear_College.set_title("Graduations_College and gap_Employment")


# In[129]:


# relation between Graduations_University and gap_Employment
linear_University = sns.regplot(x="Graduations_University", y="gap_value", data=df_2020)
linear_University.set_title("Graduations_University and gap_Employment")


# In[130]:


# relation between First_industry and gap_Employment
linear_First = sns.regplot(x="First_industry", y="gap_value", data=df_2020)
linear_First.set_title("First_industry and gap_Employment")


# In[131]:


# relation between Confirmed and gap_Employment
linear_Confirmed = sns.regplot(x="Confirmed", y="gap_value", data=df_2020)
linear_Confirmed.set_title("Confirmed and gap_Employment")


# In[132]:


# relation between Death and gap_Employment
linear_Death = sns.regplot(x="Death", y="gap_value", data=df_2020)
linear_Death.set_title("Death and gap_Employment")


# In[133]:


# relation between Death and gap_Employment
linear_Recovery = sns.regplot(x="Recovery", y="gap_value", data=df_2020)
linear_Recovery.set_title("Recovery and gap_Employment")


# In[134]:


coef_order1 = model_covid.coef_[0].argsort()[::-1] #get the order of indices of reg.coef_
x, y = [], []
for i in zip(model_covid.coef_[0][coef_order], model_covid.feature_names_in_[coef_order1]):
    y.append(i[0])
    x.append(i[1])
    print('{:.3f}'.format(i[0]), i[1])


# In[154]:


plt.figure(figsize = (40,20))
matplotlib.rcParams.update({'font.size': 30})
plt.bar(x, y)
plt.title("Feature importance of unemployment rate in 2020", size = 30)


# In[ ]:





# In[ ]:





# In[ ]:




