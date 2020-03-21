from flask import (
    Blueprint, render_template
)

bp = Blueprint('views', __name__)

# a simple page that says hello
@bp.route('/')
def index():
    return render_template('tasks/index.html')

# a simple page that says hello
@bp.route('/form')
def form():
    return render_template('tasks/form.html')
