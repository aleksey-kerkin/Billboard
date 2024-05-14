from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Announcement(models.Model):
    CATEGORIES = [
        ("Tank", "Танк"),
        ("Heal", "Хил"),
        ("DD", "ДД"),
        ("Trader", "Торговец"),
        ("Guild Master", "Гильдмастер"),
        ("Quest Giver", "Квестгивер"),
        ("Blacksmith", "Кузнец"),
        ("Tanner", "Кожевник"),
        ("Alchemist", "Зельевар"),
        ("Spellmaster", "Мастер заклинаний"),
    ]
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name="Заголовок")
    category = models.CharField(max_length=17, choices=CATEGORIES, verbose_name="Категория")
    text = CKEditor5Field(config_name="default", verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])


class Response(models.Model):
    anoncement = models.ForeignKey(
        Announcement, on_delete=models.CASCADE, verbose_name="Объявление"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(max_length=10000, verbose_name="Текст")
    status = models.BooleanField(default=False, verbose_name="Статус")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return f"Ответ на {self.post.title} от {self.user.username}"


# class Subscription(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     subscribed = models.BooleanField(default=False, verbose_name="Подписан")
