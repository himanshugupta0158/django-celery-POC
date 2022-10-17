from django.core.mail import send_mail
from celery_example.settings import EMAIL_HOST_USER

def send_mail_without_celery():
    send_mail(
        subject="Without Celery Sending Mail",
        message="It works bro, COOL",
        from_email=EMAIL_HOST_USER,
        recipient_list= [
            "himanshugupta.ongraph@gmail.com"
        ],
        fail_silently=False
    )
    return None