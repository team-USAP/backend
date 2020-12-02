from django.contrib.gis.db import models
from center.models import BaseUUIDTimeModel, City, Center
from django.contrib.auth.models import User
from users.models import Profile


class Appointment(BaseUUIDTimeModel):

    STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('waitlisted', 'Waitlisted'),
        ('rejected', 'Rejected'),
        ('arrived', 'Arrived'),
        ('failed', 'Failed'),
        ('completed', 'Completed')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(null=True, blank=True)
    leaving_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,  choices=STATUS, default='pending',)

    def __str__(self):
        return f'{self.center} {self.profile.user}'
