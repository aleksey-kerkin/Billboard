from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    tank = "TN"
    heal = "HL"
    dd = "DD"
    trader = "TR"
    guild_master = "GM"
    quest_giver = "QG"
    blacksmith = "BS"
    tanner = "TN"
    alchemist = "AL"
    spell_master = "SM"

    CATEGORIES = [
        (tank, "Танк"),
        (heal, "Хил"),
        (dd, "ДД"),
        (trader, "Торговец"),
        (guild_master, "Гильдмастер"),
        (quest_giver, "Квестгивер"),
        (blacksmith, "Кузнец"),
        (tanner, "Кожевник"),
        (alchemist, "Зельевар"),
        (spell_master, "Мастер заклинаний"),
    ]
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=2,
        choices=CATEGORIES,
        verbose_name="Название",
    )
    subscribers = models.ManyToManyField(
        User, blank=True, related_name="categories", verbose_name="Подписчики"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Announcement(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name="Заголовок")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="announcements", verbose_name="Категория"
    )
    text = CKEditor5Field(config_name="default", verbose_name="Текст")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


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
