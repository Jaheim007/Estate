from django.contrib import admin
from .models import House, HouseImage, HousePaymentPeriod, HouseReservation, HouseType, City

@admin.register(House)
class HouseInfo(admin.ModelAdmin):
    list_display = (
        'agent',
        'main_image',
        'rooms_number',
        'garage_number',
        'toillete_number',
        'address_name',
        'price',
        'price_payment',
        'house_type',
        'city',
        'latitude',
        'longitude'
    )

@admin.register(HousePaymentPeriod)
class Period(admin.ModelAdmin):
    list_display = ('name', 'isactive', 'description', 'symbol')

@admin.register(HouseImage)
class Image(admin.ModelAdmin):
    list_display = ('house', 'image')

@admin.register(HouseType)
class Type(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(HouseReservation)
class HouseReservation(admin.ModelAdmin):
    list_display = ('name','phone','comment')

@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ('name',)
    
