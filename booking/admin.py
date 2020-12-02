# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'profile',
        'center',
        'arrival_time',
        'leaving_time',
        'status',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'profile',
        'center',
        'arrival_time',
        'leaving_time',
    )
