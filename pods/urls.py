from django.urls import path
from . import views

urlpatterns = [
    path('allpods/', views.allpods, name="allpods"),
]
