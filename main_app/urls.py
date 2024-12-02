from django.urls import path
from main_app import views

urlpatterns = [
    # path('', views.Home.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
]