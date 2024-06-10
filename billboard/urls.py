from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementUserListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    ResponseCreateView,
    ResponseListView,
    ResponseUpdateView,
    ResponseDeleteView,
    approve_response,
)


urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcement_list"),
    path("<int:pk>/", AnnouncementDetailView.as_view(), name="announcement_detail"),
    path("create/", AnnouncementCreateView.as_view(), name="announcement_create"),
    path("<int:pk>/update/", AnnouncementUpdateView.as_view(), name="announcement_update"),
    path("<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcement_delete"),
    path("<int:pk>/response/create/", ResponseCreateView.as_view(), name="response_create"),
    path("response/<int:pk>/update/", ResponseUpdateView.as_view(), name="response_update"),
    path("response/<int:pk>/delete/", ResponseDeleteView.as_view(), name="response_delete"),
    path("profile/<user>/my_responses", ResponseListView.as_view(), name="response_list"),
    path("profile/<user>/my_announcements", AnnouncementUserListView.as_view(), name="profile"),
    path("response/<int:pk>/approve", approve_response, name="response_approve"),
]
