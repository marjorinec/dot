# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from times.models import Time

import gitlab
import pprint as pp

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
        
        team = get_object_or_404(Time, nome=time_slug)
    
        team.skills = ['lavar', 'passar', 'tretar', 'dançar', 'neymar']
        context['time'] = team
        
        # http://pythonbunny-memuller.c9users.io/hdjksahjdksahjkdadhsadhjkasdjkasd/
        # http://pythonbunny-memuller.c9users.io/Teste/
        # http://python-gitlab.readthedocs.io/en/stable/api-usage.html
        
        gl = gitlab.Gitlab('http://gitlab.com', 'cHCit8sbsWE1DjmkKetz')
        gl.auth()

        group = gl.groups.get('203463')
        member = group.members.list()
        project = group.projects.list()
        #milestones = project.milestones.list()
        context['gitlab_group_info'] = group
        context['gitlab_members'] = member
        context['gitlab_projects'] = project#
        # https://docs.gitlab.com/ee/api/groups.html#details-of-a-group
        
        # login: memuller ; senha: S1ndeL%1988
        
        
        
        return context

