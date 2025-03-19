from django.contrib import admin
from django.urls import path, include
from restaurant_management.kitchen import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("restaurant_management.kitchen.urls")),
    path("home/", views.HomeView.as_view(), name="home"),
]
