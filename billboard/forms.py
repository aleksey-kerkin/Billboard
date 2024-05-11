from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "text"]
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django-ckeditor-5"}, config_name="announcement"
            ),
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ["text"]
