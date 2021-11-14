#!/usr/bin/env python
# coding: utf-8

# In[1]:
#I am using flask application to direct RESTful API commands to this application.
from flask import Flask
app = Flask(__name__)

#Needed libraries
import numpy as np
import pandas as pd

#Libraries for visualisation
import plotly.express as px
import plotly.graph_objs as go
#To convert to formal date format
from datetime import date


# In[2]:

#I brought the data from ecommerce dataset and converted it to pandas object
# I removed the duplicate rows that may have been recorded twice
data = pd.read_csv('kz.csv').drop_duplicates()
data.head(5)
data.dtypes

#Arrange the data according to order_id
data.set_index('order_id', inplace=True)

#To check how many null values are in each column
null_columns = data.columns[data.isnull().any()]
data[null_columns].isnull().sum()


# In[3]:

#Check the number of unique products and users
n_unique_products = data['product_id'].nunique()
n_unique_users = data['user_id'].nunique()
print('Number of unique users: ' + str(n_unique_users) +'. Number of unique products is: ' + str(n_unique_products))


# In[4]:

#Convert the date to correct format
data['event_time']=pd.to_datetime(data['event_time'])

#Drop the values which are empty
data.dropna(subset=['category_code'],inplace=True)
#Create a new column with a simpler category code
data['category'] = data['category_code'].str.rsplit('.', n=1, expand=True)[1]


# In[8]:

#Drop old column
data.drop(columns=['category_code'], inplace=True)
#print(data['category'].head())


# In[9]:

#Rest api method of get to send the information about the best brands in terms of total revenue to the microservices
@app.route('/bestbrands', methods=['GET'])
def bestbrands():
    #Retrieve the top 5 performing brands by total revenue by grouping the brands by price
    best_brands = data.groupby('brand')['price'].sum().reset_index().sort_values('price', ascending=False).head(5)
    ar=np.array(best_brands)
    ar1=np.delete(ar, 1, axis=1)
    result=ar1.flatten()
    print(result)
    return result

# In[11]:
#Print the best performing brand in relation with the price
best_brands = data.groupby('brand')['price'].sum().reset_index().sort_values('price', ascending=False).head(5)
fig = px.bar(
    best_brands, 
    x='brand', 
    y='price', 
    title='Best performing brands',
    width=500, 
    height=500
)
fig.show()


# In[13]:
#Rest api method of get to send the information about the best brands in terms of total items to the microservices
@app.route('/mostsoldbybrands', methods=['GET'])
def mostsoldbybrands():
    #Retrieve the top 5 performing brands by total items by grouping the brands by price 
    mostsoldbybrands = data.groupby('brand')['price'].agg('count').reset_index().sort_values('price', ascending=False).head(5)
    ar=np.array(mostsoldbybrands)
    ar1=np.delete(ar, 1, axis=1)
    result=ar1.flatten()
    print(result)
    return result

#Print the best performing brand in relation with the number of items
mostsoldbybrands = data.groupby('brand')['price'].agg('count').reset_index().sort_values('price', ascending=False).head(5)
mostsoldbybrands.rename(columns={"brand": "brand", "price": "total_times_sold"}, inplace=True)
fig = px.bar(
    mostsoldbybrands, 
    x='brand', 
    y='total_times_sold', 
    title='Most sold brands',
    width=500, 
    height=500
)

fig.show()


# In[16]:
#Rest api method of get to send the information about the best selling items in terms of each category to the microservices
@app.route('/mostsoldbycategories', methods=['GET'])
def mostsoldbycategories():
    #most bought categories: most sold item in each category
    mostsoldbycategories = data.groupby('category')['price'].agg('count').reset_index().sort_values('price', ascending=False).head(5)
    ar=np.array(mostsoldbycategories)
    ar1=np.delete(ar, 1, axis=1)
    result=ar1.flatten()
    print(result)


mostsoldbycategories = data.groupby('category')['price'].agg('count').reset_index().sort_values('price', ascending=False).head(5)
mostsoldbycategories.rename(columns={"category": "category", "price": "total_times_sold"}, inplace=True)

fig = px.bar(
    mostsoldbycategories, 
    x='category', 
    y='total_times_sold', 
    title='Most sold categories',
    width=500, 
    height=500
)

fig.show()


#If there is a problem with the code, it can be debugged when connected to externel port
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


