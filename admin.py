# -*- coding: utf-8 -*-
from django.contrib import admin
from gallery.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

admin.site.register(Gallery)

# Register your models here.
