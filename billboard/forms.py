from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    text = forms.CharField(widget=CKEditor5Widget(config_name="default"))

    class Meta:
        model = Announcement
        fields = ["title", "category", "text"]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ["text"]
