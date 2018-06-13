# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=130, blank=True, null=True)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='internal_posts/',
                             verbose_name="Photo d'illustration", null=True, blank=True)

    def __str__(self):
        return self.title


class SiteContent(models.Model):
    CAT_CHOICES = (
        (1, 'Biographie FR'),
        (2, 'Biographie ENG'),
    )

    place_in_site = models.IntegerField(choices=CAT_CHOICES, verbose_name='')
    title = models.CharField(max_length=250)
    content_left = RichTextField(
        verbose_name="Texte de gauche", blank=True, null=True)
    content_right = RichTextField(
        verbose_name="Texte de droite", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SiteImageContent(models.Model):
    CAT_CHOICES = (
        (1, 'Premiere Image de fond'),
        (2, 'Fond parralaxe'),
    )

    chosen_content = models.IntegerField(choices=CAT_CHOICES, verbose_name='')
    image_file = models.FileField(upload_to='internal_posts/',
                                  verbose_name="", null=True, blank=True)
