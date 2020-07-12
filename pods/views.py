from django.shortcuts import render


def allpods(request):
    """ A view to return the all_podcasts page """

    return render(request, 'pods/allpods.html')
