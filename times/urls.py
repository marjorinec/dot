from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^times/esportes3', views.esportes3)

]
