from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Announcement(models.Model):
    tank = "TK"
    heal = "HL"
    dd = "DD"
    trader = "TR"
    guild_master = "GM"
    quest_giver = "QG"
    blacksmith = "BS"
    leather_worker = "LW"
    alchemist = "AL"
    spell_master = "SM"

    CATEGORIES = [
        (tank, "Tank"),
        (heal, "Heal"),
        (dd, "Damage Dealer"),
        (trader, "Trader"),
        (guild_master, "Guild Master"),
        (quest_giver, "Quest Giver"),
        (blacksmith, "Blacksmith"),
        (leather_worker, "Leatherworker"),
        (alchemist, "Alchemist"),
        (spell_master, "Spell Master"),
    ]
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name="Title")
    category = models.CharField(
        max_length=2, choices=CATEGORIES, default=tank, verbose_name="Category"
    )
    text = CKEditor5Field(config_name="default", verbose_name="Text")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])


class Response(models.Model):
    announcement = models.ForeignKey(
        Announcement, on_delete=models.CASCADE, verbose_name="Announcement"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    text = models.TextField(max_length=10000, verbose_name="Text")
    status = models.BooleanField(default=False, verbose_name="Status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"Response on {self.post.title} from {self.user.username}"
