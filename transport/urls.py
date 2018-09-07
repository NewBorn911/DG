from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('models', views.Models.as_view(), name='models'),
    path('trucks', views.Trucks.as_view(), name='trucks'),
]