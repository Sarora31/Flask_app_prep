from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S') 

    return render_template('index.html', day_of_week= day_of_week,current_time=current_time)

@app.route('/submit',methods=['POST'])
def submit():

    form_data = dict(request.form)

    requests.post(BACKEND_URL + '/submit',json=form_data)
                   
    return 'data submitted successfully'

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

    app.run(host='0.0.0.0',port=8000,debug=True)