from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Shows all products, sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ shows individual details of a product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)

