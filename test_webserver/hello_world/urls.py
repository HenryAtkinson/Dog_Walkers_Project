from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='hello_world-home'),
    path('about/', views.about, name='hello_world-about'),
    path('map/', views.map, name='hello_world-map'),
]