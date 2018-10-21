from django.db import models
from django.conf import settings
# Create your models here.
#


class Location(models.Model):
    railwayStation = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Employee(models.Model):
    locId = models.ForeignKey(Location, on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100, default='')
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    registrationNo = models.CharField(max_length=50)
    contactNo = models.CharField(max_length=13, default=0)
    def __str__(self):
        return str(self.id)


class Booking(models.Model):
    flags = (('Platform to Outside', 'Outside to Platform'),)
    userid = models.CharField(max_length=300)
    empId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    locId = models.ForeignKey(Location, on_delete=models.CASCADE)
    # pickupTime = models.DateTimeField(auto_now=True)
    # dropTime = models.DateTimeField(auto_now=False, default=0)
    flagIn = models.CharField(max_length=30, choices=flags, default='Platform to Outside')

    def __str__(self):
        return str(self.id)


class Rate(models.Model):
    weight = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.weight + "=" + self.rate


class Available(models.Model):
    empId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    avail = models.BooleanField(default=True)

    def __str__(self):
        return str(self.empId)

class CoolieRating(models.Model):
    coolieId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.CharField(default=5),
    review = models.TextField(null=True)

    def __str__(self):
        return str(self.id)


class CustomerRating(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, default=1)
    rating = models.CharField(default=5),
    review = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
