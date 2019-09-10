# currency-conv
A simple currency converter project


## Dependencies
1. virtualenv (venv for python3 and above)
   
   Create virtual env (let env = *filename*)
   ```sh
   python -m venv env
   ```

   Activate venv (virtual env is required to run Flask app)

   Unix
   ```sh
   source env/bin/activate
   ```

   Windows
   ```sh
   .\env\Scripts\activate 
   ```

2. package dependencies (pip requirements)
   
   ```sh
   pip install -r requirements.txt
   ```
## Running Flask

1. ```sh
   $ export FLASK_ENV=development
   $ flask run
   ```

(On Windows you need to use set instead of export.)

In the event that the above doesn't work for Windows' users, try the following with Powershell

   ```sh
   $ env:FLASK_ENV = "development"
   flask run
   ```