from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KKMREH0XWsg7HlQysZDDh12FRuEpknsaZBX9hwrLeOFu9e30lD60tSFANsa6PEziBC6PERnDEjurXvEeqY25vaB00gu6i7sJx',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
