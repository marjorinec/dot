# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=20)
    link = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
