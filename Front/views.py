from django.shortcuts import render
from .models import Banner, Service, SiteInfo, Social, Blog, Testimony, Contact, Footer
from Customers.models import Customer, InfoAgent, SocialAgent
from House.models import House, HouseImage, HousePaymentPeriod, HouseReservation, HouseType

def home(request):
    banners = Banner.objects.all()
    services = Service.objects.all()
    houses = House.objects.all()
    agents = InfoAgent.objects.all()
    social_agent = SocialAgent.objects.all()
    blogs = Blog.objects.all()
    testimonies = Testimony.objects.all()

    return render(request, 'pages/index.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())

def property(request):
    return render(request, 'pages/property-grid.html', locals())

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(
        name = name,
        email = email, 
        subject = subject, 
        message = message)

        contact.save()
    return render(request, 'pages/contact.html', locals())

def agents(request):
    return render(request, 'pages/agents-grid.html', locals())

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blog-grid.html', locals())

def property_single(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment') 
        house = request.POST.get("house")
        reservation = HouseReservation(
        name= name,
        phone = phone, 
        comment = comment,
        house = house)
        reservation.save()

    return render(request, 'pages/property-single.html', locals())

def agent_single(request):
    return render(request, 'pages/agent-single.html', locals())

def blog_single(request):
    return render(request, 'pages/blog-single.html', locals())

# Create your views here.
