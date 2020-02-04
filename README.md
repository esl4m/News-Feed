# News-Feed
Another news feed application based on python & Django


## To run the app on docker:
- Clone the repo to your local `git clone https://github.com/esl4m/News-Feed.git`
- cd into folder.
- Create .env file , you can copy .env.example then rename and edit it.
- Run the following command `docker-compose up --build -d`
- To check the status of the running containers, run the following command `docker ps -a`
- To get inside the "web" docker container using this: `docker exec -u 0 -it Container_ID bash`

- To create super user inside docker `./manage.py createsuperuser`

- Run the server like that: `./manage.py runserver` or restart the "web" container.

.....


## To run the app without docker:
- Create adn activate virtualenv: 
`virtualenv env`
`source env/bin/activate`

- Clone the repo to your local `git clone https://github.com/esl4m/News-Feed.git`

- cd into the application folder

- Create .env file , you can copy .env.example and rename your values

- Create Postgres Database and do not forget to add it to your .env file.

- Run the following commands to apply migrations for default Django Tables
`./manage.py makemigrations`
`./manage.py migrate`

- Create super user `./manage.py createsuperuser`

- Run `./manage.py runserver`

......


### To check the endpoints by url
List all entries, Create New, Update or Delete
`http://127.0.0.1:8000/api`

......

TBC

.....


Enjoy :)

