from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dish
from .forms import DishForm
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the home page!")


def index(request):
    return render(request, "kitchen/index.html")


class IndexView(TemplateView):
    template_name = "kitchen/index.html"


class HomeView(TemplateView):
    template_name = "kitchen/home.html"


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dishes"


class AddDishView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/add_dish.html"
    success_url = reverse_lazy("dish_list")


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class EditDishView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/edit_dish.html"
    success_url = reverse_lazy("dish_list")


class DeleteDishView(DeleteView):
    model = Dish
    template_name = "kitchen/delete_dish.html"
    success_url = reverse_lazy("dish_list")
