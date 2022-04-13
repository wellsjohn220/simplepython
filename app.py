from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasktodo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


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
    
@app.route("/todo", methods=['POST', 'GET'])
def todo():   
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/todo')
        except:
            return 'There was an issue adding your task'
        # return "posted value..."
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("todo.html", tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/todo')
        except:
            return 'There was an issue updating your task'
    else: 
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/todo')       
    except:
        return 'There was a problem deleting that task'

if __name__ == '__main__':
    app.run(debug=True)