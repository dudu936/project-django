from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    id = id + 1
    return render(request, 'recipes/pages/home.html')
