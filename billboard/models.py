from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

# TODO Redifine models


class Category(models.Model):
    TYPES = [
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
    name = models.CharField(max_length=17, choices=TYPES, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, related_name="categories")

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = CKEditor5Field(config_name="default", verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, verbose_name="Статус")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ на {self.post.title} от {self.user.username}"
