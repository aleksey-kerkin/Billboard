from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    ResponseCreateView,
    ResponseDeleteView,
)


urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcement_list"),
    path(
        "<int:pk>/",
        AnnouncementDetailView.as_view(),
        name="announcement_detail",
    ),
    path("create/", AnnouncementCreateView.as_view(), name="announcement_create"),
    path(
        "<int:pk>/update/",
        AnnouncementUpdateView.as_view(),
        name="announcement_update",
    ),
    path(
        "<int:pk>/delete/",
        AnnouncementDeleteView.as_view(),
        name="announcement_delete",
    ),
    path(
        "<int:pk>/response/create/",
        ResponseCreateView.as_view(),
        name="response_create",
    ),
    path(
        "<int:pk>/response/<int:response_pk>/delete/",
        ResponseDeleteView.as_view(),
        name="response_delete",
    ),
]
