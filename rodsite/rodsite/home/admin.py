# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, SiteContent

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Post, PostAdmin)


class SiteContentAdmin(admin.ModelAdmin):
    list_display = ['place_in_site', 'title',
                    'content_left', 'content_right',  'created_date']

admin.site.register(SiteContent, SiteContentAdmin)
