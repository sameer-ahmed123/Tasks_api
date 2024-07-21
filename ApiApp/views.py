from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ApiApp.serializers import TaskSerializer
from ApiApp.models import Tasks
from rest_framework import status
# Create your views here.


@api_view(["GET"])
def List_tasks(request):
    qs = Tasks.objects.all()
    serializer = TaskSerializer(qs, many=True).data
    return Response({"Tasks": serializer})


@api_view(["GET"])
def Task(request, id):
    qs = get_object_or_404(Tasks, id=id)
    serializer = TaskSerializer(qs).data
    return Response({"Task": serializer})


@api_view(["POST"])
def Create_tasks(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def Delete_task(request, id):
    qs = get_object_or_404(Tasks, id=id)
    title = qs.Task_title
    qs.delete()
    return Response({"Message": f"{title} deleted"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def Update_task(request, id):
    task_instance = get_object_or_404(Tasks, id=id)
    serializer = TaskSerializer(task_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message": f"{task_instance.Task_title} updated successfuly"}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
