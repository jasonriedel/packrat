#!/usr/bin/env python

from celery import Celery
from lib.collections import Gcp

#app = Celery('tasks', backend='amqp', broker='amqp://')
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks',  backend='rpc://', broker='amqp://guest@localhost:5672//')

# @app.task(ignore_result=True)
# def print_hello():
#     print 'hello there'
#
# @app.task
# def gen_prime(x):
#     multiples = []
#     results = []
#     for i in xrange(2, x+1):
#         if i not in multiples:
#             results.append(i)
#             for j in xrange(i*i, x+1, i):
#                 multiples.append(j)
#     return results


@app.task
def collect_instances():
    gcp = Gcp()
    gcp.create_service('compute')
    instances = gcp.collect_instances('tuxlabs-trading', 'us-west1-a')
    print instances
