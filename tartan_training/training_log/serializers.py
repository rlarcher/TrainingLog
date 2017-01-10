from rest_framework import serializers
from training_log.models import *
from django.contrib.auth import *

class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner
        fields = ('id','user','first_name','last_name','username','password','age')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('runner', 'miles', 'hours', 'minutes', 'seconds', 'note', 'day', 'month', 'year')
