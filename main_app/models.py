from django.db import models

# Create your models here.

#Моделі:
# - офер
# - послуги (фото, заголовок, текст)
# - Таблиця цін порядково (назва(текст), ціна від (варчар)
# - Контакти (варчар?)
# - Про себе (Фото, текст)
# - Роботи архів ( фото, текст)



# CharField(max_length=None, **options)
# TextField(**options)
# ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

class Offer(models.Model):
    #image
    title = models.CharField(max_length=80)
    text = models.TextField()
    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    # image
    title = models.CharField(max_length=80)
    text = models.TextField()
    link = models.CharField(max_length=80, blank=True)
    def __str__(self) -> str:
        return self.title

class MPlast_Price(models.Model):
    name = models.CharField(max_length=80)
    price = models.CharField(max_length=20)
    def __str__(self) -> str:
        return str(self.name +' ' + self.price)

class Aluminium_Price(models.Model):
    name = models.CharField(max_length=80)
    price = models.CharField(max_length=20)
    def __str__(self) -> str:
        return str(self.name +' ' + self.price)

class Wood_Price(models.Model):
    name = models.CharField(max_length=80)
    price = models.CharField(max_length=20)
    def __str__(self) -> str:
        return str(self.name +' ' + self.price)

class Contact(models.Model):
    operator = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.operator

class AboutOwner(models.Model):
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.description[:20]

class AboutStaff(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name[:20]

class AboutCompany(models.Model):
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.description[:20]

class Archive(models.Model):
    name = models.CharField(max_length=100)
    image_1 =models.ImageField(blank=True, null=True)
    image_2 =models.ImageField(blank=True, null=True)
    image_3 =models.ImageField(blank=True, null=True)
    # blank=True, null=True - gives ability to not have an image
    # for some of the instances
    description = models.TextField()
    def __str__(self) -> str:
        return self.name[:40]