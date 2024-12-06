from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('animals', views.animals, name=""),
    path('list', views.list_animals, name=""),
]