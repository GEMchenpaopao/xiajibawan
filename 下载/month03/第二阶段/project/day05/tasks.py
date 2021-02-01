from celery import Celery
import time
#1 初始化celery
app = Celery('aid2010',broker='redis://@127.0.0.1:6379/1')

@app.task
def task_test():
    time.sleep(3)
    print('task is running ...')