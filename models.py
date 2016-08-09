# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Title'))
    image = models.ImageField(upload_to="art", verbose_name=_('Image'))
    inmaine = models.BooleanField(default=False,  verbose_name='Inmaine')
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    order = models.IntegerField(blank=True, null=True, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return unicode(self.title)