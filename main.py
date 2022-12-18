
from datetime import datetime
from flask import Flask, render_template

import requests
app = Flask(__name__)

api_Agify = "https://api.agify.io"
api_Genderize = "https://api.genderize.io"
# you can write some python code in html using {{whatever}}
# To run it just type your name after the "/" in url
# e.g "http://127.0.0.1:5000/racool"

@app.route('/<string:name>')
def guessAgeGen(name):
    currentYear = datetime.now().year
    pName = name
    age = requests.get(f"{api_Agify}/?name={name}").json()["age"]
    gender = requests.get(f"{api_Genderize}/?name={name}").json()["gender"]

    return render_template("guess.html",name= pName,age=age, gender = gender,year = currentYear)



if __name__ == "__main__":
    app.run(debug=True)
