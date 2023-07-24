from os import getenv
from  redis import from_url
from rq import Queue


queue_name='default'
redis_queue=Queue(name=queue_name,connection=from_url(getenv('redis_url')))
for i in range(5):
    redis_queue.enqueue('tasks.simple_task',i)
