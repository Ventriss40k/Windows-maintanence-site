from django.contrib import admin
from .models import Service, AboutOwner, AboutCompany, AboutStaff,  Archive, Contact, Offer, MPlast_Price,Aluminium_Price,Wood_Price

models = [Service, AboutOwner, AboutCompany, AboutStaff, Archive, Contact, Offer, MPlast_Price, Aluminium_Price, Wood_Price
]

# Register your models here.


admin.site.register(models)