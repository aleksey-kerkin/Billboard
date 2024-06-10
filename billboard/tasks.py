from django.conf import settings
from django.core.mail import send_mail

from .models import Response


def notify_new_response(pk):
    response = Response.objects.get(id=pk)
    try:
        send_mail(
            subject="MMORPG - New response to your announcement!",
            message=f"Howdy, {response.announcement.user}!\n"
            f'There is a new response to your announcement "{response.announcement.title}".\n'
            f'{response.user}: "{response.text}", ',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                response.announcement.user.email,
            ],
        )
    except Exception as e:
        print("Error sending email:", e)


def notify_approved_response(pk):
    response = Response.objects.get(id=pk)
    try:
        send_mail(
            subject="MMORPG - Your response is approved!",
            message=f"Howdy, {response.user}!\n"
            f'Your response to the "{response.announcement.title}" has been accepted.\n'
            f"You can view the entire announcement at the link:\n"
            f"{settings.SITE_URL}/{response.announcement.id}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                response.user.email,
            ],
        )
    except Exception as e:
        print("Error sending email:", e)
