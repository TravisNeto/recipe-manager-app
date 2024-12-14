from django.urls import path
from . import views

urlpatterns = [
    #Home and Auth
    path('login/', views.Login.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    

    #Recipe
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
    path('recipes/<int:recipe_id>/ingredients/create/', views.ingredient_create, name='ingredient-create'),

    
    # Ingredient Views
    path('ingredients/', views.ingredient_list, name='ingredient-list'),
    path('ingredients/create/', views.ingredient_create, name='ingredient-create'),
    path('ingredients/<int:ingredient_id>/update/', views.ingredient_update, name='ingredient-update'),
    path('ingredients/<int:ingredient_id>/delete/', views.ingredient_delete, name='ingredient-delete'),

    # Step Views
    path('recipes/<int:recipe_id>/steps/', views.step_list, name='step-list'),
    path('recipes/<int:recipe_id>/steps/create/', views.step_create, name='step-create'),
    path('steps/<int:step_id>/update/', views.step_update, name='step-update'),
    path('steps/<int:step_id>/delete/', views.step_delete, name='step-delete'),

    # Favorite Views
    path('favorites/', views.FavoriteList.as_view(), name='favorite-list'),
    path('recipes/<int:recipe_id>/favorite/', views.favorite_create, name='favorite-create'),
    path('favorites/<int:favorite_id>/delete/', views.favorite_delete, name='favorite-delete'),
]

