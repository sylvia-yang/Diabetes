#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#STEP 1: Prepare data (import libraries, load the data, and clean the data)

#Import the libraries
from sklearn import datasets


# In[6]:


#Load the dataset
#This diabetes dataset is a built-in dataset in sklearn
diabetes = datasets.load_diabetes()
print(diabetes.DESCR)


# In[ ]:


#Print feature names
print(diabetes.feature_names)


# In[ ]:


#Define x and y variables
x = diabetes.data
y = diabetes.target

#check their dimension
x.shape, y.shape


# In[ ]:


#STEP 2: Split the data into training dataset (80%) and testing dataset (20%)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.2)


# In[ ]:


#check the dimensions of training set
x_train.shape, y_train.shape


# In[ ]:


#check the dimensions of testing set
x_test.shape , y_test.shape


# In[ ]:


#STEP 3: Build the model
#Import libraries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model = LinearRegression()


# In[ ]:


#STEP 4: Fit the model to train data
model.fit(x_train, y_train)


# In[ ]:


#Apply the training model to make prediction on the testing set
y_predict = model.predict(x_test)


# In[ ]:


#Print the model performance
print("The coefficient for our model is:", model.coef_)
print("The intercept for our model is:", model.intercept_)
print("Mean Squared Error (MSE) is: %.2f" % mean_squared_error(y_test,y_predict))
print("R^2 is: %.2f" % r2_score(y_test, y_predict))


# In[ ]:


print(diabetes.feature_names)


# In[ ]:


# y = -13.85*(age)-215.216*(sex)+523.072*(bmi)+346.584*(bp)-983.914*(s1)+539.403*(s2)+186.943*(s3)+266.342*(s4)+818.697*(s5)+31.08478(s6)


# In[ ]:


y_test


# In[ ]:


y_predict


# In[ ]:


#Make the scatter plot
import matplotlib.pyplot as plt
plt.scatter(y_test, y_predict, marker="d", alpha=0.5)


# In[ ]:





# In[ ]:





# In[ ]:




