from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipesViewsTest(TestCase):
    def test_recipe_home_view_is_correct(self):
        view = resolve(reverse('recipes-home'))

        self.assertIs(view.func, views.home_view)

    def test_recipe_category_view_is_correct(self):
        view = resolve(reverse('recipes-category', kwargs={'category_id': 1}))

        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(reverse('recipes-recipe', kwargs={'id': 1}))

        self.assertIs(view.func, views.recipe)
