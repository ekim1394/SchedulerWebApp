# Introduction
This web app is meant to create a website using python 3 and the Flask web framework.
Partly meant as a learning experience as well as giving something cool/useful to my mother.
- Genie

## Things to setup on your laptop (Must have permissions to run scripts)
1. pip install virtualenv
2. virtualenv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt

## How to run webapp locally
1. python run.py
2. Open browser
3. [http://localhost:5000]

## Deployment Steps for heroku
1. git commit -am "Add descriptive commit message"
2. git push
3. git push heroku master
3.(b) check for any errors in build
4. heroku ps:scale web=1
5. heroku open

## Things to do/add
Better design (CSS and wireframes perhaps)
Sidebar
More space on the edges
More assets
Google Maps API