from django.shortcuts import redirect, render
from .models import Banner, Service, SiteInfo, Social, Blog, Testimony, Contact, Footer
from Customers.models import Customer, InfoAgent, SocialAgent
from House.models import House, HouseImage, HousePaymentPeriod, HouseReservation, HouseType

def home(request):
    banners = Banner.objects.all()
    services = Service.objects.all()
    onehouse = House.objects.first()
    houses = House.objects.all()
    agents = InfoAgent.objects.all()
    social_agent = SocialAgent.objects.all()
    blogs = Blog.objects.all()
    testimonies = Testimony.objects.all()

    return render(request, 'pages/index.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())

def property(request):
    houses = House.objects.all()

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
            message = message
        )

        contact.save()
        return redirect("contact")
    return render(request, 'pages/contact.html', locals())

def agents(request):
    social_agent = SocialAgent.objects.all()
    agents = InfoAgent.objects.all()
    return render(request, 'pages/agents-grid.html', locals())

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blog-grid.html', locals())

def property_single(request, property_id):
    house_type = HouseType.objects.first()          
    try:  
          
        houses = House.objects.get(id=property_id)
        print("on a:",houses)
        return render(request, 'pages/property-single.html', locals())
    
    except:   
        
        data = {
            'msg' : 'error'
        }

        return redirect('/', data)

def agents_post_property(request):    
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment') 
        house = request.POST.get('house')
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

def filter_search(request):
    try:
        all_request_data = request.GET 
        all_house = House.objects.all()
        word = all_request_data.get("word")
        house_type = all_request_data.get("house_type")
        city = all_request_data.get("city")
        bedroom_number = all_request_data.get("bedroom_number")
        garage_number = all_request_data.get("garage_number")
        toilets_number = all_request_data.get("toilets_number")
        min_price = all_request_data.get("min_price")
        
        if house_type and int(house_type) != -1:
            all_house = all_house.filter(house_type__id = int(house_type))
        if city and int(city) != -1: 
            all_house = all_house.filter(city__id = int(city))
        if min_price and int(min_price):  
            all_house = all_house.filter(price__gte = int(min_price))
        
    
        data = {
                    "houses": all_house
                }
        return render(request, 'pages/property-grid.html', data) 
       
        
    except Exception as e:
        print("Exception ",str(e))
    
        return redirect('/')