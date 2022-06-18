from House.models import HouseType, City

def House_type(request):      
    house = HouseType.objects.all()
   
    
    return{
        'house': house
    }
    
def list_cities(request):
     city = City.objects.all()
     
     return {
        'cities': city,
     }