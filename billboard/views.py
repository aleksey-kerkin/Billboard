# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Announcement, Response
from .forms import AnnouncementForm, ResponseForm


class AnnouncementListView(ListView):
    model = Announcement
    context_object_name = "announcements"
    template_name = "announcement_list.html"
    paginate_by = 10
    ordering = ["-created"]


class AnnouncementDetailView(DetailView):
    model = Announcement
    context_object_name = "announcement"
    template_name = "announcement_detail.html"


class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcement_create.html"
    success_url = reverse_lazy("announcement_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcement_update.html"
    success_url = reverse_lazy("announcement_list")


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = "announcement_delete.html"
    success_url = reverse_lazy("announcement_list")


class ResponseCreateView(CreateView):
    model = Response
    form_class = ResponseForm
    context_object_name = "response"
    template_name = "response_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class ResponseUpdateView(UpdateView):
#     model = Response
#     form_class = ResponseForm
#     template_name = "response_update.html"
#     success_url = reverse_lazy("announcement_list")


class ResponseDeleteView(DeleteView):
    model = Response
    template_name = "response_delete.html"
    success_url = reverse_lazy("announcement_list")
