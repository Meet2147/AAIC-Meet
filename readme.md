# AAIC-Python-Quiz
Simple quiz app to run on command line displays options for the user to select and then asks questions 
according to the selection and displays the score finally.
## Running the quiz app
```python3 aaic.py```
## _quiz.json_
The file is a static file with only two groups Sport and Maths.Can make changes to the file
or add our own file.
## Dockerfile
```
FROM python:3.7
COPY aaic.py .
COPY quiz.json .
CMD python3 aaic.py
```
## Creating docker image using the docker file 
```docker build  docker build -t python-quiz .```
## Running docker image 
```docker run -ti python-quiz```
## Docker image 
Use this [https://hub.docker.com/repository/docker/mdockj/aaic-quiz]
## Pull the docker image using following command
```docker pull mdockj/aaic-quiz```