from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("dishes/", views.dish_list, name="dish_list"),
    path("dish/add/", views.add_dish, name="add_dish"),
    path("dish/<int:pk>/", views.dish_detail, name="dish_detail"),
    path("dish/edit/<int:pk>/", views.edit_dish, name="edit_dish"),
    path("dish/delete/<int:pk>/", views.delete_dish, name="delete_dish"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
