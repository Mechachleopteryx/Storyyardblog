from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog', blog, name="blog"),
    path('detail/<str:pk>', detail, name="detail"),
    path('search', search_results, name='search'),
    path('contact', contact, name='contact'),
]
