# Build and Run a Docker Container for Ecommerce Machine Learning Model

The idea is to do a quick and easy build of a Docker container with a simple machine learning model and run it. In order to start building 2 Docker containers for a machine learning model and using kafka and docker compose to help communicate between them. let’s consider five files: 
-	Dockerfile
-	Ecommerce_recommendation1.py
-   Ecommerce_recommendation2.py
-   docker-compose.yml
-   kz.csv

The Ecommerce_recommendation1.py is a python script that ingest and normalize data in a csv file (kz.csv) and train 3 models to get information on best brands by revenue, best item for each brand and get the best selling items for each category. This can then be accessed by other microservices via restful api. There is a port exposed to connect to the calculated information. The calculated information is sent to kafka under topic of Ecommerce which broadcast 
to information under producer.

The Ecommerce_recommendation2.py is a python script that consumes the data from Ecommerce and plots the graph under another docker container. 

Dockerfile is used to build the image for my application. The necessary libraries are installed and files are moved to the docker image. A port is exposed to send information via restful api to the other microservices.

kz.csv has the dataset of Ecommerce events history electronics shop which has over 20 million data points. The file contains purchase data from April 2020 to November 2020 from a large home appliances and electronics online store. The dataset contains columns of event_time,order_id,product_id,category_id,category_code,brand,price,user_id.

Docker compose is a yaml file which is used to build and containerise both kafka and zookeeper. Docker Compose is used to automate the deployment and scaling.

Docker commands to build the container:
Build the image from the dockerfile:  sudo docker image build -t flaskEco .
Run the image inside a container: sudo docker run flaskEco python3 xp.py
You will be able to retrieve the information about mostsoldbycategories, mostsoldbybrands, bestbrands via restful api under port 5000. Eg: http://127.0.0.1:5000/mostsoldbycategories for the most item sold under each category. 
sudo docker ps: You are able to check the running container.
sudo docker stat: You are able to check the resources being used up by the running docker container.
sudo docker stop _id: Once you are completed with the testing, you can stop the running container.

Docker commands to startup docker compose:
To start up kafka brokers and zookeeper: docker-compose up -d
Check the running containers: docker ps
Check the network: docker network ls
There are three default networks — bridge, host, null. The 4th network is created by docker compose which connects kafka and zookeeper : docker network inspect < bridge name>
PRODUCER SIDE: $ docker exec -it <kafka container name or id> bash
Check the topics in kafka: /opt/kafka/bin/kafka-topics.sh --list --zookeeper
Create a new topics in kafka: /opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test2
List topics: /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181
Start a producer to publish data stream from input to kafka: /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic test-topic
CONSUMER SIDE: /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test-topic
