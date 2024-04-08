import time

from celery import shared_task


@shared_task
def slow_operation():
    time.sleep(3)
