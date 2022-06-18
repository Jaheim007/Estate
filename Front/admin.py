from django.contrib import admin
from .models import Banner, Contact, SiteInfo, Service, Blog, Testimony, Social

@admin.register(Banner)
class Slide(admin.ModelAdmin):
    list_display = ('title', 'title_number', 'address', 'address_number', 'image')

@admin.register(Social)
class SocialInfo(admin.ModelAdmin):
    list_display = ('facebook_link','instagram_link','twitter_link', 'linkedin_link', 'main_phone', 'email', 'latitude', 'longitude' )

@admin.register(SiteInfo)
class Site(admin.ModelAdmin):
    list_display = ('title', 'main_color', 'full_site_color', 'default_mode')

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title', 'type')

@admin.register(Testimony)
class Testimony(admin.ModelAdmin):
    list_display = ('name', 'description', )

@admin.register(Contact)
class ContactInfo(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
