from django.contrib import admin
from django.urls import path, include
from kitchen import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("kitchen/", include("kitchen.urls")),
    path("", views.index, name="index"),
]
