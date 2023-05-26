from django.contrib import admin
from .models import *

class AdminProfile(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Offer)
admin.site.register(Aboutus)
admin.site.register(Blog)
admin.site.register(WorkPictures)