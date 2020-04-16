import os

from flask import Flask
from markupsafe import escape
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

from application.views import latest_tasks

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    Bootstrap(app)
    datepicker(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'application.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/tasks/new', endpoint='new_task')
    app.add_url_rule('/tasks/<int:id>/update/', endpoint='update_task')
    app.add_url_rule('/tasks/<int:id>/delete/', endpoint='delete_task')

    from .database import db_session

    #@app.teardown_appcontext
    app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


    return app
