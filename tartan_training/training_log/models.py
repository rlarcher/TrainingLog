from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Runner(models.Model):
  user = models.OneToOneField(User)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  age = models.IntegerField()
  picture = models.ImageField(upload_to="user_images",blank=True)

  def __unicode__(self):
    return self.username


class Workout(models.Model):
  runner = models.ForeignKey(Runner)
  miles = models.FloatField()
  hours = models.IntegerField()
  minutes = models.IntegerField()
  seconds = models.IntegerField()
  note = models.CharField(max_length=60)
  day = models.IntegerField()
  month = models.IntegerField()
  year = models.IntegerField()
