from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipes-home.html')
