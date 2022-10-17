from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from celery_example.settings import EMAIL_HOST_USER

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    send_mail(
        subject="Mail sent Using dajngo-Celery",
        message="It worked faster, Celery is cool",
        from_email=EMAIL_HOST_USER,
        recipient_list = [
            "himanshugupta.ongraph@gmail.com"
        ],
        fail_silently=False
    )

    return None
