from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name = "home"),
    #path("", views.home_there, name = "home_there"),
]