from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view),
    path('recipes/<int:id>/', views.recipe)
]
