from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_Route, name='get_Route'),
    path('lobby/', views.chart_view, name='landing'),
    path('', views.chart_view, name='landing'),



]