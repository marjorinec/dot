# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import gitlab

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'times/home.html', {})

def esportes3(request):
    gl = gitlab.Gitlab('http://gitlab.com', 'cHCit8sbsWE1DjmkKetz')
    gl.auth()

    groups = gl.groups.list()


    return render(request, 'times/esportes3.html', {})
