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


class AnnouncementUserListView(ListView):
    model = Announcement
    context_object_name = "announcements"
    template_name = "announcement_user_list.html"
    paginate_by = 10
    ordering = ["-created"]

    def get_queryset(self):
        return Announcement.objects.filter(user=self.request.user)


class AnnouncementDetailView(DetailView):
    model = Announcement
    context_object_name = "announcement"
    template_name = "announcement_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["responses"] = Response.objects.filter(announcement=self.object)
        return context


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
    template_name = "announcement_create.html"

    def get_success_url(self):
        announcement = Announcement.objects.get(pk=self.kwargs["pk"])
        return reverse_lazy("announcement_detail", args=[announcement.pk])


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
        form.instance.announcement_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        announcement = Announcement.objects.get(pk=self.kwargs["pk"])
        return reverse_lazy("announcement_detail", args=[announcement.pk])


class ResponseListView(ListView):
    model = Response
    template_name = "response_list.html"
    context_object_name = "responses"

    def get_queryset(self):
        return Response.objects.filter(user=self.request.user)


class ResponseUpdateView(UpdateView):
    model = Response
    form_class = ResponseForm
    template_name = "response_create.html"
    success_url = reverse_lazy("announcement_list")

    # def get_queryset(self):
    #     # Получаем объявление по pk
    #     announcement = get_object_or_404(Announcement, pk=self.kwargs["pk"])
    #     # Фильтруем ответы по объявлению и текущему пользователю
    #     return Response.objects.filter(announcement=announcement, user=self.request.user)

    # def get_success_url(self):
    #     announcement = Announcement.objects.get(pk=self.kwargs["pk"])
    #     return reverse_lazy("announcement_detail", args=[announcement.pk])


class ResponseDeleteView(DeleteView):
    model = Response
    template_name = "response_delete.html"
    success_url = reverse_lazy("announcement_list")

    # def get_success_url(self):
    #     announcement = Announcement.objects.get(pk=self.kwargs["pk"])
    #     return reverse_lazy("announcement_detail", args=[announcement.pk])
