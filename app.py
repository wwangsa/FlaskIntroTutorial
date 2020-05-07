from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

""" 
    freecodeCamp Learn flask for Python tutorial
    https://www.youtube.com/watch?v=Z1RJmh_OqeA
"""

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    completed= db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

#rendering HTML template
@app.route('/', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        #get data submitted from the text field by name
        task_content = request.form['txtcontent']
        new_task = Todo(content=task_content)
        #adding entry into database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was issue adding the order"
    else:
        #Get data from sqllite
        dbtasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=dbtasks)

#Creating route for delete command passing ID
@app.route('/delete/<int:id>')
def delete(id):
    #get the id, if the id not exist, pass 404 page
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect ('/')
    except:
        return 'There was a problem deleting the task'

#Creating route for update
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    #get the id, if the id not exist, pass 404 page
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        #Setting the content so don't need to use db command
        task.content = request.form['txtcontent']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your tasks'

    else:
        return render_template('update.html', task = task)


if __name__ == "__main__":
    app.run(debug=True)
