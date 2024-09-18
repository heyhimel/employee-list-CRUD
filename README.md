This web project is built with Django and PostgreSQL. This project will allow you to insert, delete, update, sort and read data( Name, Birthdate, Picture, Email and Mobile number) with pagination.

1. To run this project, you have to follow this instructions
2. Virtual environment creation=>
3. Open cmd and type
"pip install virtualenv"
open any folder. type "virtualenv myvirtualenvname"
4. To work with virtal environment, it needs to activate,
from cmd,  go to "myvirtualenvname" folder=> "Scripts" folder => type "activate"
5. Django envionment creation
in cmd "pip install Django
in cmd "pip install Pillow"
6. Now install PostgreSQL for database, do yourself
Install psycopg2 "pip install psycopg2"
7. Database connection with PostgreSQL
   7.1 Create database by typing in cmd line "createdb -U your_database_user your_database_name"
   7.2 write password "1234"
   7.3 database name "employee"
9. Go to "assignment" folder
10. In cmd "python manage.py makemigrations"
11. In cmd "python manage.py migrate"
12. Now you are ready to go
13. Run your server from cmd
Type "python manage.py runserver"
