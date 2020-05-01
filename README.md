# Docker_Project
Here you will build a web application using Python and HTML code running on Docker compose.
The application uses the Flask framework and maintains a hit counter in Redis.

## Prerequisites:
Make sure you have already installed both **Docker** and **Docker-Compose** in your system.

## Setup:
1. Open Terminal.
2. Change the current working directory to the location where you want the cloned directory to be made.
3. Type the below given command.  
> $ git clone https://github.com/SuruchiKalnaik/Docker_project.git
4. Press Enter. Your local clone will be created.

## Description:
Here four files will be created. First is ***app.py***, it is a python file where code is written for calculation of the hit counts along with HtML code integrated with it.    
Second one is ***requirement.txt***. Here there is a list of all dependencies which need to be downloaded.    
Third one is ***Dockerfile*** that builds a Docker image. The image contains all dependencies the web application requires including Python itself.   
Fourth one is ***docker-compose.yml*** file which will define services in compose file. This compose file defines two services: web and redis.
The web service uses an image that's build from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port 5000.
This example service uses the default port for the Flask web server i.e. 5000. The redis service uses a public Redis image pulled from Docker Hub.   

## Running the test:
From your project directory, start up your application by running   
> $ docker-compose up       

Then enter http://localhost:5000/ in your browser to see the application running.   

## Output:
Your window will look like     
      
![Output1](https://user-images.githubusercontent.com/64151370/80817444-0d9c1980-8bef-11ea-8968-8585fb12ec7e.png)

When you refresh your page it will increase the count.

![Output2](https://user-images.githubusercontent.com/64151370/80817894-e134cd00-8bef-11ea-9740-54fb9b792527.png)
   
Finally your complete website has been created just by single command along with the database and now you will able to interact with it.
