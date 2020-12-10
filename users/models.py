from django.contrib.gis.db import models
from center.models import BaseUUIDTimeModel, City
from django.contrib.auth.models import User


class Profile(BaseUUIDTimeModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
        ('U', 'Unknown'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='U')
    phone_no = models.PositiveBigIntegerField(null=True, blank=True)
    aadhar_card = models.PositiveBigIntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)

    covid_vacc = models.BooleanField(default=False)
    BLOOD = (
        ('A+', 'A+ Type'),
        ('B+', 'B+ Type'),
        ('AB+', 'AB+ Type'),
        ('O+', 'O+ Type'),
        ('A-', 'A- Type'),
        ('B-', 'B- Type'),
        ('AB-', 'AB- Type'),
        ('O-', 'O- Type'),
        ('NA', 'Not Available')

    )
    bloodType = models.CharField(max_length=10, choices=BLOOD, default='NA')
    allergy = models.CharField(max_length=100, null=True, blank=True)
    alzheimer = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    stroke = models.BooleanField(default=False)
    comments = models.CharField(max_length=700, null=True, blank=True)

    def __str__(self):
        return f'{self.user} '


class Location(BaseUUIDTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = models.PointField()

    def __str__(self):
        return f'{self.user}'
