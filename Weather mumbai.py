#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df= pd.read_csv("C:/PYTHON DATA SETS/archive/pblds.csv")
print(df.head(10))


# In[4]:


print(df.shape)


# In[5]:


print(df.info())


# In[6]:


print(df.isnull().sum())


# In[7]:


print(df.describe().T)


# In[8]:


print(df.head(10))


# In[9]:


print(df.columns)


# In[10]:


df.columns=['day','hour','temp','humidity','windspeed','winddirection']


# In[11]:


print(df.head(10))


# In[12]:



plt.scatter(df.windspeed,df.temp,color='blue')
plt.savefig('image/foo.png')
plt.show()

# In[13]:



plt.scatter(df.humidity,df.temp,color='blue')
plt.show()

# In[14]:



plt.scatter(df.winddirection,df.temp,color='blue')
plt.show()

# In[15]:


wdata=df.copy()


# In[16]:


print(wdata.head())


# In[17]:


pdata=wdata.drop(['day','hour'],axis=1)


# In[18]:


print(pdata.head())


# In[19]:


y=pdata.temp


# In[20]:


X=pdata.drop('temp',axis=1)


# In[21]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, accuracy_score, mean_squared_error


# In[22]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=50)


# In[23]:


lr= LinearRegression()
lr.fit(X_train,y_train)


# In[24]:


print("Linear Regression R^2 Score: {:.4f}%".format(lr.score(X_test, y_test)*100))
y_pred = lr.predict(X_test)

print("Linear Regression RMSE: {:.4f}".format(np.sqrt(mean_squared_error(y_test, y_pred))))


# In[28]:


print(X_train.iloc[45])


# In[26]:


wpred=lr.predict([[73.776042,15.904271,259.469583]])[0]
print(wpred)


# In[27]:


import pickle
with open('model.pickle','wb') as f:
  pickle.dump(lr,f)

