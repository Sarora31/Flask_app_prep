from flask import Flask, request,   render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#seeting up mongo db server using mongocloud and .env file for saftey
load_dotenv()

uri = os.getenv("MONGO_URI")   # if using dotenv
client = MongoClient(uri)

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S') 

    return render_template('index.html', day_of_week= day_of_week,current_time=current_time)

#storing of data on a mongodb server using flask server
@app.route('/submit', methods=['POST'])
def submit():
    
    form_data = dict(request.form)

    collection.insert_one(form_data)
    
    return 'data submitted successfully'

@app.route('/view')
def view():
    data =collection.find()

    data = list(data)
    
    for item in data:

     print(item)
    
     del item['_id']
 
    data ={
       'data':data

    }
    
    return data

    """
    name = request.form.get('name')

    print(request.args)
    return 'Hello, ' + name + '!'
    """
# decleratio of  variable in jinja is {{ _name of varianle called in backed }} 

#---------------------------------
"""
#section 1 for app route
@app.route('/')
def home():

    return 'hello Guys  come on '

"""
#----------------------------------
"""
#section 7 rendering a html cass page using rendering template
@app.route('/html/')
def html():

    return render_template('index.html')
"""
#-----------------------------------
"""
# section 6 of route app calling using Json 
# How to call a route on website after api'?' and after each vairable & for seperation 
#  http://127.0.0.1:5000/api?age=12&name=yahoo

@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')
    
    age =int(age)

    if age > 18:

        return 'You are Welcome to use the website, ' + name + "!"
    
    else:
        
        return 'sorry you are too young to use the website'
'''
    result={
        'Name': name,
        'Age': age
    }
'''
"""

    #return result
"""
#------------------
#section 5 of the route app calling using function and variables
#return a sum of  values fucntion
@app.route('/add/<a>/<b>')
def name(a,b):
    
    #if we use int in flask for return a function then it give eroro so we uese dictonary

    # result = int(a)+ int(b)

    # TypeError: The view function did not return a valid response. The return type must be a string, dict, list, tuple with headers or status, Response instance, or WSGI callable, but it was a int.

    answer = int(a)+int(b)

    result = {
        'ans' : answer
    }
    
    return result
"""
#-------------------------

#section 2 for app route calling using a route 
#return a value function using flask
"""
@app.route('/api/<name>')
def name(name):

    result = "Hello " +'\fn' + name + "!"

    return result

"""
#-------------------------

# section 3 of app route  calling using url
#creating another page 

"""
@app.route ('/second')
def second():                                                       

    return " welcome to second page"
"""
#-------------------------------------

#section 4 for app route calling using a function.
#route to define an api "/api/"<name> here is a variable.
"""
@app.route('/api/<name>')
def name(name):
    
    length =len(name)

#section 4 part 1 for app route        
@app.route('/api/<name>')           
    if length > 5:

        return " Name is too Long!!!"
    
    else:

        return 'Nice name!!!'
"""
# we have defined the application here but 
# we have yet to run the application so syntax to run a applicationi s below.
#or we can say call function of the app

if __name__ == '__main__':

    app.run(debug=True)