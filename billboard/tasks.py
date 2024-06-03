from django.conf import settings
from django.core.mail import send_mail

from .models import Response


def notify_new_response(pk):
    print("Notify new response called")
    response = Response.objects.get(id=pk)
    print("Email:", response.announcement.user.email)
    try:
        send_mail(
            subject="MMORPG - new response to your announcement!",
            message=f"Привет, {response.announcement.user}!\n"
            f'На ваше объявление "{response.announcement.title}" есть новый отклик.\n'
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
    send_mail(
        subject="MMORPG - your response is approved!",
        message=f"Привет, {response.user}!\n"
        f'Ваш отклик на объявление "{response.announcement.title}" принят.\n'
        f"Посмотреть объявление целиком можно по ссылке:\n"
        f"{settings.SITE_URL}/{response.announcement.id}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[
            response.user.email,
        ],
    )
