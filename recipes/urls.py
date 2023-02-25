from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='recipes-home'),
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
    path('recipes/category/<int:category_id>',
         views.category, name='recipes-category'),
]
