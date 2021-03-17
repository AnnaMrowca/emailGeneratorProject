from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')


def email(request):

    email_length = int(request.POST.get('length'))
    email_provider = request.POST.get('domain')

    numbers = string.digits
    letters = string.ascii_letters

    email_intro = ''
    email_domain = ''

    for i in range(email_length):
        if request.POST.get("numbers"):
            email_intro += random.choice(numbers + letters)
        else:
            email_intro += random.choice(letters)

    if email_provider == 'Gmail':
        email_domain = '@gmail.com'
    if email_provider == 'Proton':
        email_domain = '@protonmail.com'
    if email_provider == 'Yahoo':
        email_domain = '@yahoo.com'

    final_email = email_intro + email_domain

    return render(request, 'generator/email.html', {'finalEmail': final_email})

