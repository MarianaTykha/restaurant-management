from django.db import models
from django.utils.translation import gettext_lazy as _


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Dish Type")
        verbose_name_plural = _("Dish Types")

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    image = models.ImageField(upload_to="dishes/", null=True, blank=True)
    servings = models.IntegerField(default=1)
    date_added = models.DateTimeField(
        auto_now_add=True
    )  # Додано поле для дати додавання страви

    class Meta:
        verbose_name = _("Dish")
        verbose_name_plural = _("Dishes")

    def __str__(self):
        return self.name

    def get_total_price(self):
        return self.price * self.servings


class Chef(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = _("Chef")
        verbose_name_plural = _("Chefs")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
