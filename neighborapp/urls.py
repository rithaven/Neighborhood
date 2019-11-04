from django.conf.urls import url
from .import views


urlpatterns=[
  url(r'^$', views.home, name='home'),
  url(r'^neighborhood/(/d+)',views.neighborhood,name=neighborhood),
  url(r'^profile/(\d+)',views.profile,name='profile'),
  url(r'^add_business/',views.add_business,name='add_business'),
  url(r'^change_neighborhood/(\d+)',)
]