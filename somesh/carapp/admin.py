from django.contrib import admin
from .models import Car

admin.site.register(Car)
class caradmin(admin.ModelAdmin):
    list_display = ('car_id','brand','model','year','price')


