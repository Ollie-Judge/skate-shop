from django.shortcuts import render

# Create your views here.

def contact(request):
    """
    oversees the contact us page form
    """

    return render(request, 'contact/contact.html')