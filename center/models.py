from django.contrib.gis.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import uuid

from django.contrib.auth.models import User


class BaseUUIDTimeModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class City(BaseUUIDTimeModel):
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.state}'


class Center(BaseUUIDTimeModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(
        max_length=200,
        help_text='Name of the Center',
        validators=[MinLengthValidator(
            limit_value=5, message="Minimum Length of 5 ")],
    )

    slug = models.SlugField(max_length=255, unique=True)

    # Logo image of the center
    logo = models.ImageField(default='project_header/default.png',
                             upload_to='project_header', blank=True, null=True)
    # backdrop image of center
    header_image = models.ImageField(default='default.png',
                                     upload_to='project_logo', blank=True, null=True)

    # For Site-wide on off switch
    published = models.BooleanField(default=True)
    # For Reviewed and Verified Centers
    reviewed = models.BooleanField(default=False)
    # For Featured Section on main page
    featured = models.BooleanField(default=False)

    location = models.PointField()
    address = models.CharField(max_length=100)

    city = models.ForeignKey(
        City, related_name='centres', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Center, self).save(*args, **kwargs)

    def publishedFlip(self, *args, **kwargs):
        self.published = not self.published
        try:
            self.save(*args, **kwargs)
        except:
            ValidationError("Internal Server Error")

    def reviewFlip(self, *args, **kwargs):
        self.reviewed = not self.reviewed
        try:
            self.save(*args, **kwargs)
        except:
            ValidationError("Internal Server Error")

    class Meta:
        verbose_name = "Center"
        verbose_name_plural = "Centers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Center_detail", kwargs={"pk": self.pk})


# Views
# Register - Multistage
# Login - username , password - Center, User - dashboard
# Dashboards - Stock, Availability Change and Location
# Appointment View - sortby distance , time
# Appointment Detail View - User Data (Med, Contact,) - Delete , Reschedule ( Email ) - completed then user is vaccinated
# User
# Register - Phone , Email, Username, Password - account
# User Dashboard - Profile Add View - Blood Group , (TBD)
# User Main -  Map View , List View ( Centres ) | JS Script automic hidden form submit location
# Appointment Create View - Time ,
# Nearby vaccinated user maps views
# Vaccinated Check Tick - key Vaccinated
