from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("list",views.list_persons, name='list'),
    path("create",views.create_persons, name='list')
]
