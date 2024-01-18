from django.shortcuts import render

# Create your views here.

# Naming here is selected by user


def index(request):
    meetups = [
        {
            'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'
        },
        {
            'title': 'A second Meetup', 'location': 'Bogotá', 'slug': 'a-second-meetup'
        }
    ]
    # the path is relative to the templates folder
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

# A view is a function and by default, it requires a request parameter


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {'title': 'A First Meetup',
                       'description': 'This is the first meetup'}
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
