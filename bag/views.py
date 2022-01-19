from django.shortcuts import render


def view_bag(request):
    """ renders the shopping cart page """

    return render(request, 'bag/bag.html')