from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish
from .forms import DishForm
from django.http import HttpResponse


def index(request):
    return render(request, "kitchen/index.html")


def home(request):
    return HttpResponse("Welcome to the kitchen!")


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, "kitchen/dish_list.html", {"dishes": dishes})


def add_dish(request):
    if request.method == "POST":
        form = DishForm(
            request.POST, request.FILES
        )  # Додаємо request.FILES для завантаження зображення
        if form.is_valid():
            form.save()
            return redirect("dish_list")
    else:
        form = DishForm()
    return render(request, "kitchen/add_dish.html", {"form": form})


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, "kitchen/dish_detail.html", {"dish": dish})


def edit_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(
            request.POST, request.FILES, instance=dish
        )  # Додаємо request.FILES
        if form.is_valid():
            form.save()
            return redirect("dish_list")
    else:
        form = DishForm(instance=dish)
    return render(request, "kitchen/edit_dish.html", {"form": form})


def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        dish.delete()
        return redirect("dish_list")
    return render(request, "kitchen/delete_dish.html", {"dish": dish})
