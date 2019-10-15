# sccServer


This is the back-end of the [SCC Front](https://github.com/rocontrex/sccFront). 

It's a RESTful API built with Python + Django + MySql that receive all the data related with employees and processes status and record/provide to the client all this data through a REST API. 

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

To run this project in the development mode, you'll need to have a basic environment with Python 3 installed. To use the database, you'll need to have MySql Server installed and running on your machine.

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
