from django.contrib import admin
from django.urls import path, include
from kitchen import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("kitchen.urls")),
    path("home/", views.HomeView.as_view(), name="home"),
]
