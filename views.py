# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Gallery
from django.template import Context, loader

def index(request):
    gallery_list = Gallery.objects.order_by('order')
    context = {'gallery': gallery_list}
    return render(request, 'gallery/index.html', context)
