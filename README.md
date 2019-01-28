### 1. Go to the dir with manage.py file and run server
cd messages

python manage.py runserver

Note! Redis should be running.
### 2. Run Websocket Server in python
python server.py

### 3. Run Websocket client

python client.py



### 4. Open in your browser http://127.0.0.1:8000/chat/alert/ 
and wait, because 95% of the distribution lies within two standard deviations of the mean.


## ABOUT

Server continuously sends numberand its sequence number sampling from a normal distribution with parameters (0, 1).


Websocket client reads a stream server and for each value that over 2 standart deviation range of the mean 
create an log message that includes a current timestamp, number and and its sequence number.



