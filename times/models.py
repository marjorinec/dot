# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=20)
    gitlab_team_link = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    slacker_link = models.CharField(max_length=100, null=True)
    github_link = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.nome
