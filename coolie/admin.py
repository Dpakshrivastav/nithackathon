from django.contrib import admin
from .models import Location, Employee, Booking, Rate, Available, CustomerRating, CoolieRating
# Register your models here.
admin.site.register(Location)
admin.site.register(Employee)
admin.site.register(Booking)
admin.site.register(Rate)
admin.site.register(Available)
admin.site.register(CustomerRating)
admin.site.register(CoolieRating)