from django.shortcuts import render

# Create your views here.

# Naming here is selected by user


def index(request):
    meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A second Meetup'}
    ]
    # the path is relative to the templates folder
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
