from rest_framework import serializers
from training_log.models import *

class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner
        fields = ('id','user','first_name','last_name','username','password','age')

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('runner', 'miles', 'hours', 'minutes', 'seconds', 'note', 'day', 'month', 'year')
