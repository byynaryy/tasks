from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from application.models import Task
from application.database import db_session

bp = Blueprint('views', __name__)


#
@bp.route('/')
@bp.route('/tasks/')
def index():
    tasks = db_session.query(Task).all()
    return render_template('tasks/index.html', tasks=tasks)

#
@bp.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        db_session.add(
            Task(
                title = request.form['title'],
                description = request.form['description'],
                status = request.form['status'],
                initialised = request.form['initialised']
            )
        )
        db_session.commit()
        return render_template('tasks/index.html')
    else:
        return render_template('tasks/newtask.html')

#
@bp.route('/tasks/<int:id>/update/', methods=['GET', 'POST'])
def update_task(id):
    task = db_session.query(Task).filter_by(id=id).one()
    if request.method == 'POST':
        task.title = request.form['title'],
        task.description = request.form['description'],
        task.status = request.form['status'],
        task.initialised = request.form['initialised']
        db_session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('tasks/updatetask.html', task=task)

#
@bp.route('/tasks/<int:id>/delete/', methods=['GET', 'POST'])
def delete_task(id):
    task = db_session.query(Task).filter_by(id=id).one()
    db_session.delete(task)
    db_session.commit()
    return redirect(url_for('index'))

#
@bp.context_processor
def latest_tasks():
    latest = db_session.query(Task).order_by(Task.id)[0:3]
    return dict(latest=latest)
