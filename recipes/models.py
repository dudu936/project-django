from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField()
    description = models.CharField(max_length=165)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_time_unit = models.CharField(max_length=65)
    preparation_time = models.IntegerField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipe/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, null=True,
        default=None, blank=True,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, null=True, default=None
    )

    def __str__(self):
        return self.title
