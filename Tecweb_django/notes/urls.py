from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listatags', views.listatags, name='listatags'),
  #  path('tag/<str:tag_>/', views.tag, name='tag'),
]