from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class User(User):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MeasurementQty(models.Model):
    quantity = models.FloatField()

    def __str__(self):
        return str(self.quantity)

#Links recipes and ingredients with associated quantities and units.
class RecipeIngredient(models.Model): 
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe_ingredients")
    measurement_qty = models.ForeignKey(MeasurementQty, on_delete=models.CASCADE, related_name="recipe_ingredients")
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE, related_name="recipe_ingredients")

    def __str__(self):
        return f"{self.ingredient.name} - {self.measurement_qty.quantity} {self.measurement_unit.name}"


class Step(models.Model):
    text = models.TextField()
    step_num = models.PositiveIntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

    class Meta:
        ordering = ['step_num']

    def __str__(self):
        return f"Step {self.step_num}"


class Favorite(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favorites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")

    def __str__(self):
        return f"{self.recipe.title}"


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('entree', 'Entree'),
        ('dessert', 'Dessert'),
    ]

    type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return f"{self.type}"
