
#what is celery?
#celery is a distributed task queue system which is written in python
#which allows u to run time consuming tasks in the background - instead of making the user to wait
#example:
#send emails to 100 users
#process the uploaded images
#verify the documents
#u dont want the user to wait until the task done. so you offload the tasks to celery-> it will handle them asychronously

from celery import Celery

app=Celery(
    "tasks",#celery app
    broker="redis://localhost:6379/0", #it is a queue system where tasks are sent for workers to pick up-> once worker sees the tasks in the queue.. pulls the task message from the broker.. executes the function with the arguments.. and store results in redis db.. your code can retrieve it with .get()
    backend="redis://localhost:6379/0", #it stores the results
)
@app.task #task
def add(x,y):
    return x+y

#in python cmd
#res=add.delay(4,6) #creates a task message that contains task name(main.add) arguments(4,6) task id(uuid) this message is sent to the broker(redis)
