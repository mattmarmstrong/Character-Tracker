from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Room)
admin.site.register(Sheet)
# admin.site.register(Feature)
# admin.site.register(Equipment)
