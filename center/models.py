from django.contrib.gis.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import uuid


class Center(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4().hex[:11],
        editable=False)
    name = models.TextField(
        max_length=500,
        help_text='Name of the Center',
        validators=[MinLengthValidator(
            limit_value=20, message="Minimum Length of 20 ")],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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

    # takes in x,y,z and srid
    location = models.PointField()

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
        return self.title

    def get_absolute_url(self):
        return reverse("Center_detail", kwargs={"pk": self.pk})
