# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile, Location


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'user',
        'gender',
        'phone_no',
        'dob',
        'address',
        'city',
        'covid_vacc',
        'bloodType',
        'allergy',
        'alzheimer',
        'asthma',
        'diabetes',
        'stroke',
        'comments',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'user',
        'dob',
        'city',
        'covid_vacc',
        'alzheimer',
        'asthma',
        'diabetes',
        'stroke',
    )


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'user',
        'location',
    )
    list_filter = ('created_date', 'modified_date', 'user')
