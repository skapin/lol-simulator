# from flask_sqlalchemy import SQLAlchemy

import flask

from flask_cors import CORS
from flask_restful import Api
from celery import Celery
from flask_sqlalchemy import SQLAlchemy


class FlaskCelery(Celery):

    def __init__(self, *args, **kwargs):

        super(FlaskCelery, self).__init__(*args, **kwargs)
        self.patch_task()

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
                else:
                    with _celery.app.app_context():
                        return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app
        self.config_from_object(app.config)


db = SQLAlchemy()
cors = CORS()
rest_api = Api()
celery = FlaskCelery('tasks',
                     broker='redis://' + 'redis',
                     backend='redis://' + 'redis',
                     include=['tasks.tasks', 'tasks'])
