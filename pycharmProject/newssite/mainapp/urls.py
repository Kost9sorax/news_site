from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index),
    path('create', views.create, name='create'),
    path('tag/<str:tag>/', views.tag_list, name='tag_list'),
]
