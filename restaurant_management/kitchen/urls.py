from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("dishes/", views.DishListView.as_view(), name="dish_list"),
    path("dish/add/", views.AddDishView.as_view(), name="add_dish"),
    path("dish/<int:pk>/", views.DishDetailView.as_view(), name="dish_detail"),
    path("dish/edit/<int:pk>/", views.EditDishView.as_view(), name="edit_dish"),
    path("dish/delete/<int:pk>/", views.DeleteDishView.as_view(), name="delete_dish"),
]
