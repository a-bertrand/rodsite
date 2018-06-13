# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Ajout des modèles
from .models import Post, SiteContent

# Create your views here.
""" Pour infos :
CAT_CHOICES = (
        (1, 'Biographie FR'),
        (2, 'Biographie ENG'),
    )
"""


def index(request):
    bio_fr = SiteContent.objects.filter(place_in_site=1).first()
    bio_eng = SiteContent.objects.filter(place_in_site=2).first()
    return render(request, 'index.html', locals())
