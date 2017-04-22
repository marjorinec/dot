# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from times.models import Time

import gitlab

from django.shortcuts import render

# Create your views here.


class HomeView(TemplateView):
    template_name = 'times/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['times'] = Time.objects.all()
        return context


class TimeView(TemplateView):
    template_name = 'times/time.html'

    def get_context_data(self, **kwargs):
        context = super(TimeView, self).get_context_data(**kwargs)
        time_slug = kwargs['time_slug']
        context['time'] = get_object_or_404(Time, nome=time_slug)

        return context

    def outro_get_context_data(self, **kwargs):
        context = super(TimeView, self).outro_get_context_data(**kwargs)

        #context['time_gitlab_api'] = {'nome': 'esportes3', 'email': ''}

        gl = gitlab.Gitlab('http://gitlab.globoi.com', 'ezPYwmrp3eAsiYm5x9Aj')
        gl.auth()

        groups = gl.groups.list()
        context['time_gitlab_api'] = groups

        return context
