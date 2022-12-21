"""bikestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import add_customer, add_vehicle, add_rental
from rent.views import AddCustumerView, AddVehicleView, AddRentalView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("new-customer/", add_customer),
    # path("new-vehicle/", add_vehicle),
    # path("new-rental/", add_rental),
    path("new-customer/", AddCustumerView.as_view()),
    path("new-customer/", AddVehicleView.as_view()),
    path("new-customer/", AddRentalView.as_view()),
]
