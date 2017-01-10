from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from training_log.models import *
from training_log.serializers import *

@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def runner(request):
    if request.method == 'GET':
        runners = Runner.objects.all()
        serializer = RunnerSerializer(runners, many=True)
        print request.user
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RunnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def runner_detail(request, pk):
    """
    Retrieve, update or delete a runner instance.
    """
    try:
        runner = Runner.objects.get(pk=pk)
    except runner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RunnerSerializer(runner)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RunnerSerializer(runner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        runner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def workout(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workout_detail(request, pk):
    """
    Retrieve, update or delete a workout instance.
    """
    try:
        workout = Workout.objects.get(pk=pk)
    except Workout.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
