from django.contrib import admin
from buildings.models import ApartmentTypes, Buildings, Floors, Apartment, SimpleApartment

# admin.site.register(ApartmentTypes)
# admin.site.register(Buildings)
# admin.site.register(Floors)
# admin.site.register(Apartment)

class SimpleApartmentAdmin(admin.ModelAdmin):
    model = SimpleApartment
    readonly_fields=('id',)
    list_display = ('id', 'name')

admin.site.register(SimpleApartment, SimpleApartmentAdmin)