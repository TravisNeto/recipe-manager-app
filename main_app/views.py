from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Home view - to do
# class Home(LoginView):
#     template_name = 'home.html'

#Sign up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/recipes/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

# Create a recipe
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description']
    success_url = '/recipes/'
    #template_name = 'create.html'

# View all recipes
class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe

#View individual recipe details
class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description']
    success_url = '/recipes/'

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'