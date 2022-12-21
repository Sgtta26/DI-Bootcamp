from django.urls import path
from .views import phone_number,name

urlpatterns = [
    path('phone_number',phone_number, name= 'phone_number'),
    path('name/<str:name>',name, name= 'name'),
]

