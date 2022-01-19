from django.shortcuts import render, redirect


def view_bag(request):
    """ renders the shopping cart page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ adds specified number of selected products to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag [item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
