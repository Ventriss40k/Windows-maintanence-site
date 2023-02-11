from django.shortcuts import render, HttpResponse
from .models import Offer, Service, Contact, AboutOwner,AboutCompany,AboutStaff, Archive, MPlast_Price, Aluminium_Price, Wood_Price

def index(request):
    context = {
        'offer': Offer.objects.all(), 'service':Service.objects.all(), 'm_plast_price': MPlast_Price.objects.all(), 'aluminium_price': Aluminium_Price.objects.all(),'wood_price': Wood_Price.objects.all(), 'contact':Contact.objects.all()
    }
    return render(request, 'main_app/index.html', context)
    # return(HttpResponse("It's working"))

def about(request):
    context = {
        'about_owner': AboutOwner.objects.all(),
        'about_company': AboutCompany.objects.all(),
        'about_staff': AboutStaff.objects.all()
    }
    return render(request, 'main_app/about.html', context)

def archives(request):
    context = {
        'archives': Archive.objects.all()
    }
    return render(request, 'main_app/archives.html', context)

def client_contact_form(request):
    context = {
        'contact':Contact.objects.all()
    }
    return render(request, 'main_app.client_contact_form.html', context)