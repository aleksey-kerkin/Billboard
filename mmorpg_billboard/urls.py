from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from billboard.views import custom_upload_function

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("billboard.urls")),
]

urlpatterns += [
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("upload/", custom_upload_function, name="custom_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
