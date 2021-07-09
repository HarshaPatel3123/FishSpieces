# FishSpieces Prediction 

### Description
This is a web application designed to show the project structure for a machine learning model deployed using flask. This project features a machine learning model that has been trained to detect whether or not an online comment is which Spiece of Fish. 
This application acts as an interface for a user to submit new queries. The machine learning model was built using various features of scikit learn

First clone the repo locally.

Create a new virtual environment in the project directory.
```bash
python3 -m venv env
```
Activate the virtual environment.
```bash
env/Scripts/activate
```
While in the virtual environment, install required dependencies from requirements.txt.
```bash
pip install -r ./requirements.txt
```
Now we can deploy the web application via
python app.py

and navigate to http://127.0.0.1:5000/ to see it live. On this page, a user can then submit text into the text field and receive predictions from the trained model

### How to deploy flask app on heroku
 1) log on to Heroku
 2) Create a new app 
 3) Navigate to Deployment method and Connect with GitHub
 4) Search for the repository name
 5) Manually deploy this repo to get a link hosted by heroku
 6) Visit the link and receive predictions from the model 

