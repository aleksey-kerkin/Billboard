from django import forms

from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "text", "created"]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ["text", "created"]
