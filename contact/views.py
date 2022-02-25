from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from skate_shop import settings
from .forms import ContactForm


# Create your views here.

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ContactForm(request.GET)
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_mail(f"a message has been recieved from {email}", subject, message, [settings.EMAIL_HOST_USER])
            messages.success(request, "Message successfully sent. We will reply to you shortly")
            return render(request, "contact/contact.html", {"form":form})
    else:
        messages.error(request, "Error, message not sent")
        return render(request, "contact/contact.html", {"form":form})

    return render(request, "contact/contact.html", {"form":form})

