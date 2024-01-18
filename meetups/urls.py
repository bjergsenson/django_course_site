from django.urls import path
from . import views  # from this folder import views

urlpatterns = [
    path('meetups/', views.index)  # our-doimain.com/meetups
]
