#!/usr/bin/env python
# coding: utf8
# pylint: disable=ungrouped-imports
from __future__ import absolute_import

import logging

from server.extensions import celery
# from server.extensions import db
from server.app import create_app


LOG = logging.getLogger(__name__)

app = celery  # pylint: disable=invalid-name
app.init_app(create_app())


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        (60 * 30),
        andon_scheduler_task.s(),
    )


@app.task
def andon_scheduler_task():
    LOG.info('Andon Scheduler')


if __name__ == '__main__':
    print('=========== STARTED CELERY IN MAIN MODE ===========')
    app.start()
