from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_Route, name='get_Route'),
    path('/poops', views.poops, name='poops'),
    # path('t', views.get_Route, name='get_Route'),
    # path('tt', views.get_Route, name='poops'),



]