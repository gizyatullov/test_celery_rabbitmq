from celery_app import fib_task
from time import sleep

if __name__ == '__main__':
    tasks_list = [10, 100, 56]
    for task in tasks_list:
        sleep(1)
        fib_task.delay(task)
