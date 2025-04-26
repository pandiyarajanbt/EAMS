from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from management.serializers import TaskSerializer
from management.models import Task


class TaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


    def search(self, request):
        tasks = request.data.get('title')
        if tasks:
            tasks = Task.objects.filter(title__icontains=tasks)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_404_NOT_FOUND)
