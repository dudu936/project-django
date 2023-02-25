from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# Create your views here.


def home_view(request):
    recipes = Recipe.objects.all().filter(is_published=True)
    return render(request, 'recipes/pages/home.html', context={
                  'recipes': recipes
                  }
                  )


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.all().filter(
        category__id=category_id, is_published=True)
    )
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    }
    )


def recipe(request, id):
    recipe = get_object_or_404(Recipe, is_published=True, id=id)
    return render(request, 'recipes/pages/recipes-home.html', context={
        'recipe': recipe,
        'detail_page': True,
        'title': f'{recipe.title}'
    }
    )
