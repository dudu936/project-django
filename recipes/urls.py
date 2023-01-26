from django.urls import path

from .views import home_view

urlpatterns = [
    path('teste/', home_view)
]
