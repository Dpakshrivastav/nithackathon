from django.db import models
from django.conf import settings
# Create your models here.
#


class Location(models.Model):
    railwayStation = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Employee(models.Model):
    locId = models.ForeignKey(Location, on_delete=models.CASCADE)
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    registrationNo = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Booking(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    empId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    locId = models.ForeignKey(Location, on_delete=models.CASCADE)
    pickupTime = models.DateTimeField(auto_now=True)
    dropTime = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.id


class Rate(models.Model):
    weight = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.Weight + "=" + self.rate


