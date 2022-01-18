from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ Shows all products, sorting and searching """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
        if not query:
            messages.error(request, "No information was entered")
            return redirect(reverse('products'))
        
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ shows individual details of a product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)

