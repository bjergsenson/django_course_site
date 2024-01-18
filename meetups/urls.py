from django.urls import path
from . import views  # from this folder import views

urlpatterns = [
    # our-doimain.com/meetups the name parameter is used to identify an url on html template
    path('meetups/', views.index, name='all-meetups'),
    # to use dynamic content we can use <> a convertor is needed to match the exact format
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
