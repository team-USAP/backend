
from django.contrib import admin
from .models import Center, City, Slot
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin


@admin.register(Center)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'address', 'city')
    prepopulated_fields = {'slug': ['name']}


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('center', 'start_time', 'end_time', 'capacity')
