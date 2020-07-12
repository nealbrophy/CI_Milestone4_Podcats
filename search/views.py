from django.shortcuts import render, redirect
import requests
from django.conf import settings


def search(request):
    """ A view to return the search page """
    if "q" in request.GET:
        new_search = request.GET['q'].replace(' ', '%20')

        url = f'https://listen-api.listennotes.com/api/v2/search?q={new_search}'

        headers = {
            'X-ListenAPI-Key': settings.LISTEN_KEY,
        }
        response = requests.request(
            'GET', 
            url, 
            headers=headers
            )
        context = {
            "search_term": request.GET['q'],
            "results": response,
        }

        return render(request, 'search/search.html', context)
    else:
        return render(request, 'search/search.html')
