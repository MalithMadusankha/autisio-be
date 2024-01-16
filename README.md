# autisio-be : LookAfter

This application is designed for children to assess whether they may have autism 
and, if so, determine the level of their condition along with identifying specific 
areas of concern. The app, built using React Native for the mobile front-end and 
FastAPI for the back-end server, incorporates machine learning and face detection 
technologies. This comprehensive tool aims to provide valuable insights into a 
child's potential autism spectrum disorder, offering a nuanced understanding of 
their specific challenges.

## Technologies 

OpenCV, Mediapipe, MongoDB, FAST-API, Python

## Algorithms  

LogisticRegression, KNeighborsClassifier, and DecisionTreeClassifier

Create virtual envirment : python -m venv myenv

ACTIVATE VENV: source myenv/Scripts/activate

CONDA env: source C:/Users/Malith/anaconda3/Scripts/activate condamyenv

Create Requirment File: pip freeze > requirements.txt

requirement.text install: pip install -r requirements.txt

RUN SERVER: uvicorn index:app --reload

Test Api: http://localhost:8000/docs

kadawatha location : 8.311352,80.403651
Anuradhapura: 8.311352,80.403651
app psw: axsrbizmfuepylid

Mongodb Detaisl

password: oWfBHWmnl77NQYao

username: admin

How to deploy App in Gcloud
git clone
cd project-name
virtualenv env
source env/bin/activate
pip install -r requirements.txt
run app - gunicorn -w 4 -k uvicorn.workers.UvicornWorker index:app

How to create conda env
conda create --name myenv python=3.10.11

conda install -c conda-forge uvicorn fastapi

conda install scikit-learn=1.2.2

conda install pandas

conda install -c anaconda pymongo

Run App

uvicorn index:app --reload

change port and run

uvicorn index:app --port 8001

ngrok http 8000

zip lambda_function.zip -u mian.py
