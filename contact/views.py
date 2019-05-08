from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, [settings.EMAIL_HOST_USER])
            messages.error(request, "Thanks for contacting us!")

    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})