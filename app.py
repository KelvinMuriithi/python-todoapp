from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
from flask_migrate import Migrate
from models import db
from models import Todo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)
db.init_app(app)

# Define APIS
# get
# POST

@app.route('/tasks',methods=['POST'])
def tasks():
     if request.method =='POST':
          newTodo = Todo(task_title ='Learn python', task_description = '', task_status = 'Complete')
          db.session.add(newTodo)
          db.session.commit()
          return jsonify(newTodo)
          





if __name__ == '__main__':  
     app.run()
