from django.conf.urls import include, url
from times.views import HomeView, TimeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<time_slug>[\w-]+)/$', TimeView.as_view(), name='time_page'),
]

#a
