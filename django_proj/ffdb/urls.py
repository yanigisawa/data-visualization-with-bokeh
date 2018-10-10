from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single', views.index_single, name='index_single')
]