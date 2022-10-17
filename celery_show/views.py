from django.shortcuts import render
from django.http import HttpResponse

from .helper import *
from .task import *


def index(request):
    # sleepy(10) # wait for 10 seconds
    # sleepy.delay(30)
    # send_mail_without_celery()
    send_mail_task.delay()
    return HttpResponse(f"<h1>Hello,Using celery and Sending mail by {EMAIL_HOST_USER}</h1>")




