from django.contrib import admin
from .models import InfoAgent, Customer, SocialAgent

@admin.register(InfoAgent)
class Info(admin.ModelAdmin):
    list_display = ('customer', 'Biographie', )

@admin.register(SocialAgent)
class SocialInfo(admin.ModelAdmin):
    list_display = ('social_agent', 'name')

@admin.register(Customer)
class Custom(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image', 'birth_date', 'user_type')


# Register your models here.
