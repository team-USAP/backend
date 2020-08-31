# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Center


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created',
        'updated',
        'slug',
        'logo',
        'header_image',
        'published',
        'reviewed',
        'featured',
    )
    list_filter = ('created', 'updated', 'published', 'reviewed', 'featured')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
