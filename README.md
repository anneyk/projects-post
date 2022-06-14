# projects-post
# Description  
This project allows users to post their projects for other users to rate according to design, usability and content.
##  Live Link  
https://projects-post.herokuapp.com/
   
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To access the project  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/anneyk/projects-post.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-post 
```
```bash 
pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
```
```bash
- source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
## Technology used  
  
* Python3  
* Django 1.11  
* Heroku  
  
## License 

* Copyright (c) 2022 **Annet Khavere**
