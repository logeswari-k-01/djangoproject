from django.urls import path
from .views import index, aboutpage

urlpatterns = [
    path("home/",index),
    path("about/",aboutpage)
]