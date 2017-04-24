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


        if not "//" in team.github_link:
            team.github_link = "http://" + team.github_link

        if not "//" in team.slacker_link:
            team.slacker_link = "http://" + team.slacker_link


        context['time'] = team


        gl = gitlab.Gitlab('http://gitlab.com', 'cHCit8sbsWE1DjmkKetz')
        gl.auth()


        groups = gl.groups.search(team.nome)

        group = False

        if len(groups) == 0:
            raise Exception("Troca os nomes do grupo aaaaaaaaaa")

        else:
            for i in range(0, len(groups), 1):
                if groups[i].web_url == team.gitlab_team_link:
                    group = groups[i]
                    break


        if group == False :
            raise Exception("Troca os nomes do grupo")

        member = group.members.list()
        project = group.projects.list()
        #milestones = project.milestones.list()
        context['gitlab_group_info'] = group
        context['gitlab_members'] = member
        context['gitlab_projects'] = project

        return context
