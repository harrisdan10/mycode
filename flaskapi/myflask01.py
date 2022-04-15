#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask, redirect, url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

@app.route('/login/<stranger>')
def login(stranger):
    if stranger not in ["Gary", "Giovanni", "Jesse"]:
        #properly welcome
        # return redirect(url_for("hello_world"), name=stranger)
        return redirect(f'/pokemon/{stranger}')
    else:
        return "Blasting off again!!"

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/pokemon/<name>")
def hello_world(name):
   return f"Welome to the world of pokemon {name}"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
