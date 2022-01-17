from django.shortcuts import render


def index(request):
    """ this view returns the index page in the home folder """

    return render(request, 'home/index.html')


