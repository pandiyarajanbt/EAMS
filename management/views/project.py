from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from management.serializers import ProjectSerializer, BusinessUnitSerializer
from management.models import Project, BusinessUnit


class ProjectView(APIView):
    def post(self, request):
        project_serializer = ProjectSerializer(data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_201_CREATED)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        projects = Project.objects.all()
        project_serializer = ProjectSerializer(projects, many=True)
        return Response(project_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        project = Project.objects.get(pk=pk)
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_200_OK)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def search(self, request):
        projects = request.data.get('name')
        if projects:
            projects = Project.objects.filter(name__icontains=projects)
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
