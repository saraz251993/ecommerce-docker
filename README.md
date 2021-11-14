# Build and Run a Docker Container for Ecommerce Machine Learning Model

The idea is to do a quick and easy build of a Docker container with a simple machine learning model and run it. In order to start building a Docker container for a machine learning model, let’s consider three files: 
-	Dockerfile
-	Ecommerce_recommendation.py
-   kz.csv

The Ecommerce_recommendation.py is  a python script that ingest and normalize data in a csv file (kz.csv) and train 3 models to get information on best brands by revenue, best item for each brand and get the best selling items for each category. This can then be accessed by other microservices via restful api. There is a port exposed to connect to the calculated information.

Dockerfile is used to build the image for my application. The necessary libraries are installed and files are moved to the docker image. A port is exposed to send information via restful api to the other microservices.

kz.csv has the dataset of Ecommerce events history electronics shop which has over 20 million data points. The file contains purchase data from April 2020 to November 2020 from a large home appliances and electronics online store. The dataset contains columns of event_time,order_id,product_id,category_id,category_code,brand,price,user_id.

Docker commands to build the container:
Build the image from the dockerfile:  sudo docker image build -t flaskEco .
Run the image inside a container: sudo docker run flaskEco python3 xp.py
You will be able to retrieve the information about mostsoldbycategories, mostsoldbybrands, bestbrands via restful api under port 5000. Eg: http://127.0.0.1:5000/mostsoldbycategories for the most item sold under each category. 
sudo docker ps: You are able to check the running container.
sudo docker stat: You are able to check the resources being used up by the running docker container.
sudo docker stop _id: Once you are completed with the testing, you can stop the running container.

The dataset file :kz.csv is too large so it can be downloaded at https://www.kaggle.com/mkechinov/ecommerce-purchase-history-from-electronics-store. Thanks
