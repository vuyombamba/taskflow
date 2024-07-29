from flask import Blueprint, jsonify, request, render_template
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get('title')
    new_task = Task(title=task_title)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added!"})

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks]
    return jsonify(task_list)
