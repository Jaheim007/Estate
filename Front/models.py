from django.db import models

class SiteInfo(models.Model):     
    title = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255)
    full_site_color = models.CharField(max_length=255)
    default_mode = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Contact(models.Model): 
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Social(models.Model):
    facebook_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    main_phone = models.CharField(max_length=20) 
    email = models.EmailField(max_length=50)  
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5 , decimal_places=2)

       
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

      
    def __str__(self):
        return self.facebook_link


class Banner(models.Model):
    title = models.CharField(max_length = 255) 
    title_number = models.CharField(max_length=255)
    address = models.CharField(max_length = 255)      
    address_number = models.CharField(max_length = 255)         
    image = models.URLField()

    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    Date = models.DateField()
    image = models.URLField()

    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Testimony(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Footer(models.Model):
    network = models.ForeignKey(Social , on_delete=models.CASCADE)
    description = models.TextField()
    copyright = models.CharField(max_length=255)

    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name



