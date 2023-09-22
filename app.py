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
          newTodo = Todo(task_title ='Do Laundry', task_description = '', task_status = 'InComplete')
          db.session.add(newTodo)
          db.session.commit()
          return jsonify({'message': 'Task updated successfully', 'task': {
               'id': newTodo.id,
               'task_title': newTodo.task_title,
               'task_description': newTodo.task_description,
               'task_status': newTodo.task_status
               }})

# update
@app.route('/update/<int:task_id>', methods=['PUT'])
def update_tasks(task_id):
     if request.method == 'PUT':
          updateTask = Todo.query.get(task_id)
          if updateTask is None:
           return jsonify({'message': 'Task not found'}), 404
      
          data = request.json
          updateTask.task_title = data.get('task_title', updateTask.task_title)
          updateTask.task_description = data.get('task_description', updateTask.task_description)
          updateTask.task_status = data.get('task_status', updateTask.task_status)


          db.session.commit()
          return jsonify({'message': 'Task updated successfully', 'task': {
          'id': updateTask.id,
          'task_title': updateTask.task_title,
          'task_description': updateTask.task_description,
          'task_status': updateTask.task_status
          }})

      
      


    









       

