from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    sNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.sNo}-{self.title}"

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        Title=request.form['title']
        Desc=request.form['desc']
        query1= Todo(title=Title, desc=Desc)
        with app.app_context():
            db.session.add(query1)
            db.session.commit()
            allTodos = Todo.query.all()
        return render_template('index.html',allTodos=allTodos)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
