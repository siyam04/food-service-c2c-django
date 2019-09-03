# A web application (C2C) for delivery of hygienic foods from home to the clients.
* Live: https://food-service-c2c.herokuapp.com/
* Developed By Django Web Framework.

## Instructions (Windows 10x64):
* Some commands may differ depending on OS. Just google it.

* Install latest version of Python3 (64 bit).

* Install virtual environment:
  1. Open cmd
  2. :~$ pip install virtualenv 
  3. Choose destination: :~$ cd Desktop> virtualenv YourEnvironmentName
  
* Clone this GitHub repository into local machine.

* Go to project directory (GitHub repository) where 'manage.py' file exist.

* Copy 'YourEnvironmentName' folder to the 'GitHub repository'.

* Active virtual environment:
  1. :~$ cd YourEnvironmentName\Scripts>
  2. :~$ activate
  3. (YourEnvironmentName):~$ This '(YourEnvironmentName)' sign will be shown up if virtual environment activated successfully.
  4. :~$ cd../.. (exit from Scripts)

* Install all the requirements using previously opened CMD where the virtual environment was activated:
  >> (YourEnvironmentName):~$ pip install -r requirements.txt
  
* Run Local Server:
  >> (YourEnvironmentName):~$ python manage.py runserver

* PATHs:
  1. System Admin Dashboard: http://127.0.0.1:8000/admin/ (default)
  2. Homepage: http://127.0.0.1:8000/
  
## Homepage:
![foodservice ui](https://user-images.githubusercontent.com/23103980/49749826-7a99d100-fcd3-11e8-9b59-569323d6ebf3.png)
