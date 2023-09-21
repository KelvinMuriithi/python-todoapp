from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Todo(db.Model): 
    __tablename__ = 'my_tasks'
    id = db.Column(db.Integer, primary_key = True)
    task_title = db.Column(db.String(200),nullable= False)
    task_description = db.Column(db.String(200), nullable = True)
    task_status = db.Column(db.String(200), nullable =False)

