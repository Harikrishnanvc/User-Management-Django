
# User Management System

This project is a user management application using Postgresql as database


## Requirements

Python 3.10.2 or higher

Django 4.2 or higher

PostgreSQL

## Installation

Clone the repository

```
https://github.com/Harikrishnanvc/User-Management-Django.git
```
Install the dependencies
```
pip install -r requirements.txt    
```
# Usage
Create a postgresql database on you local (make sure you have all privileges)

Create a .env file and add all the credentials required for the database connection and add django secret-key as well.

## Migrate
Go to path 
#### User-Management-Django/user_management/
To apply migrations
```
python3 manage.py makemigrations
```


To make changes in database
```
python3 manage.py migrate

```

## Run

To start the application, run the following command:
Make sure your location is inside user_management folder
```
python3 manage.py runserver

```
The application will be running on http://localhost:8000.

## URLS
#### Register users
First get into this url for registering new user
```http
  GET http://127.0.0.1:8000/users/register/
```
#### Register users

```http
  POST http://127.0.0.1:8000/users/register/
```
* `first_name`: The user's first_name.
* `last_name`: The user's last_name.
* `email`: The user's email address.
* `mobile`: The user's phone number.
* `country`: The user's current country location
* `nationality`: The user's nationality
* `password`: The user's password.


#### Login Page

```http
  GET http://127.0.0.1:8000/users/login/
```

#### Login 

```http
  POST http://127.0.0.1:8000/users/login/
```
* `email`: The user's email address.
* `password`: The user's password.


User will be redirect to specific page according to the specific user role
