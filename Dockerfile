#Mention the base image 
FROM jupyter/scipy-notebook

#Make a new directory
RUN mkdir my-model

#Install the required libraries
#Since i am using a few libraries, i didnt use a requirements file
RUN pip install numpy
RUN pip install pandas
RUN pip install plotly

#Copy the current data file to docker
COPY kz.csv ./kz.csv

#Copy the python file with the codes into docker
COPY Ecommerce_recommendation.py ./Ecommerce_recommendation.py

#Expose the port within docker 
# With this, other applications can be connected to docker to get the required data
EXPOSE 5000

#container start up command to run the python file
CMD python3 Ecommerce_recommendation.py
