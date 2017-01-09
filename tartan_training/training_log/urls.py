from django.conf.urls import include, url
from django.contrib.auth.models import User
from training_log import views

urlpatterns = [
  url(r'^workouts/$', views.workout),
  url(r'^runners/$', views.runner),
  url(r'^runners/(?P<pk>[0-9]+)/$', views.runner_detail),
  url(r'^workouts/(?P<pk>[0-9]+)/$', views.workout_detail),
]
