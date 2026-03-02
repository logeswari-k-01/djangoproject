from django.urls import path
from .views import index,help_page

urlpatterns = [
    path("home/",index),
    path("help/",help_page)
]