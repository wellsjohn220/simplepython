from flask import Flask, render_template

app = Flask(__name__)

thisdict =	{
  "brand": "Ford",  "model": "Mustang",  "year": 2022,  "made": "Australia",  "door": 5,
  "power": 2.5,  "power window": "Yes"
}

fruits = ["apple", "banana", "cherry", "peach", "more"]

@app.route("/")
def index():   
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forloop")
def forloop():
    return render_template("forloop.html", fruits=fruits)

@app.route("/dict")
def dict():
    return render_template("dict.html", passinfo=thisdict)
    

if __name__ == '__main__':
    app.run(debug=True)