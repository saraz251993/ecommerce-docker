#!/usr/bin/env python
# coding: utf-8

# In[1]:
#I am using flask application to direct RESTful API commands to this application.
from flask import Flask
app = Flask(__name__)

#Needed libraries
import numpy as np
import pandas as pd

#Gather requests
from flask_restful import Resource, Api
import requests
	
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
#Libraries for visualisation
import plotly.express as px
import plotly.graph_objs as go
#To convert to formal date format
from datetime import date

# In[9]:

#Rest api method of get to send the information about the best brands in terms of total revenue to the microservices
@app.route('/visualizebestbrands', methods=['GET'])
#Print the best performing brand in relation with the price after receiving from API
def vizbestbrands():
    best_brands = requests.get('http://0.0.0.0/bestbrands')
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
@app.route('/visualizemostsoldbybrands', methods=['GET'])
def vizmostsoldbybrands():
#Print the best performing brand in relation with the number of items
    mostsoldbybrands = requests.get('http://0.0.0.0/mostsoldbybrands')
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
@app.route('/visualizemostsoldbycategories', methods=['GET'])
def vizmostsoldbycategories():
#Print the most sold items by categories
    mostsoldbycategories  = requests.get('http://0.0.0.0/mostsoldbycategories')
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


