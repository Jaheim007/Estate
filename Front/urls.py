from django.urls import path
from .views import home, about, contact, property, property_single, blog, blog_single, agents, agent_single , filter_search

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('property', property, name='property'),
    path('contact', contact, name='contact'),
    path('agents', agents, name='agents'),
    path('blog', blog, name='blog'),
    path('property_single', property_single, name='property_single'),
    path('agent_single', agent_single, name='agent_single'),
    path('blog_single', blog_single, name='blog_single'),   
    path('search',filter_search,name="search")
]