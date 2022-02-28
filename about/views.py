from django.shortcuts import render

# Create your views here.


def about(request):
    """
    renders the about page
    """

    return render(request, 'about/about.html')
