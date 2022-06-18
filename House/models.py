from django.db import models
from Customers.models import Customer


class HouseType(models.Model): 
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True) 
    description = models.TextField(null=True)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class HousePaymentPeriod(models.Model):
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True)
    description = models.TextField(null=True) 
    symbol = models.CharField(max_length=5)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name

class City(models.Model): 
    name = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)  
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class House(models.Model): 
    agent = models.ForeignKey(Customer , on_delete=models.CASCADE , related_name="customer_houses")   
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_houses") 
    main_image = models.URLField()
    house_number = models.CharField(max_length=150)
    house_id = models.CharField(max_length=255)
    rooms_number = models.IntegerField()
    garage_number = models.IntegerField()
    toillete_number = models.IntegerField()
    address_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    price_payment = models.ForeignKey(HousePaymentPeriod , on_delete=models.CASCADE)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address_name
    
class HouseImage(models.Model):
    house = models.ForeignKey(House , on_delete=models.CASCADE , related_name="house_houseimage")
    image = models.URLField()
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.house         
    
class HouseReservation(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_house")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    comment = models.TextField()

    is_delete = models.BooleanField(default=False)   
    created_at = models.DateTimeField(auto_now=True,null= True,blank= True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name()

    

# Create your models here.
