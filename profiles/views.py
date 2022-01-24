from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """
    displays the users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated')

    form = UserProfileForm(instance=profile)
    orders= profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'ordeers': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is confirmation of your order history refering to order number: {order_number}.'
        'A confirmation was sent on the date of this order.'
    ))

    template = 'checkout/checkout_successs/html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
