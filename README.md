# sccServer


This is the back-end of the [SCC Front](https://github.com/rocontrex/sccFront). 

It's a RESTful API built with Python + Django + Sqlite that receive all the data related with employees and processes status and record/provide to the client all this data through a REST API. 

The main purpose of this API is calculate and provide daily, monthly and yearly datas of all processes in the client's commerce, this repository was created with the intent of reuse this service to others applications, and you can get all files and use inside your own context.
  

Also, you can use this Project as you wish, be for study, be for make improvements or earn money with it!

  
It's free!

## Getting Started

### Virtualenv

Create a new virtualenv
```
python -m venv python3
```
Start the virtualenv created
```
CD python3
CD Scripts
activate
```
### Prerequisites

To run this project in the development mode, you'll need to have a basic environment with Python 3 installed. To use the database, you'll need to have sqlite Server installed and running on your machine.

### Installing

**Cloning the Repository**

```
$ git clone https://github.com/rocontrex/sccServer

$ cd sccServer
```

**Installing dependencies**

```
$ pip install -r requirements.txt
```

### Running the Development environment

Now, you'll need to change to development branch:
```
$ git checkout development
```

With all dependencies installed, the Database running and the environment properly configured, you can now run the server:

```
$ python manage.py runserver
```

### Running the Development environment

To create a new migrate run:

```
$python manage.py migrate
```

After this, will be necessary create a super user as admin, running:

```
$python manage.py createsuperuser
```

Now you can access localhost:8000/admin and create you others users.
If you need create or modify one table, you will need create a new migrate file in corresponding app.
Exemple: If you need create a migration in employee, you will need execute:

```
$pyhon manage.py makemigration employee
```

After this run

```
$pyhon manage.py migrate employee 0001
```

Where 0001 is the number of migration file created inside the migrations app folder, in this exemple will be: ./employee/migrations.

If you need see the querry thay will be executed, run:

```
$python manage.py sqlmigrate employee 001
```