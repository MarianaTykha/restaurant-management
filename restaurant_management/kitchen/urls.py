from django.urls import path
from . import views

urlpatterns = [
    path("dishes/", views.dish_list, name="dish_list"),
    path("dishes/add/", views.add_dish, name="add_dish"),
    path("dishes/<int:pk>/edit/", views.edit_dish, name="edit_dish"),
    path("dishes/<int:pk>/delete/", views.delete_dish, name="delete_dish"),
    path("dishes/<int:pk>/", views.dish_detail, name="dish_detail"),
]
