from django.shortcuts import render
from django.http import HttpResponse
from .models import  Contact


# Create your views here.


def index(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/index.html')
