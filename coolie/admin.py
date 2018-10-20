from django.contrib import admin
from .models import Location, Employee, Booking, Rate, Available
# Register your models here.
admin.site.register(Location)
admin.site.register(Employee)
admin.site.register(Booking)
admin.site.register(Rate)
admin.site.register(Available)


