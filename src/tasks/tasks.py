from __future__ import absolute_import
from server.extensions import celery


@celery.task
def start_default(app):
    print('empty')
