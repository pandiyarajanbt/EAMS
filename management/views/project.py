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
    
        

class BusinessUnitView(APIView):
    def post(self, request):
        business_units = BusinessUnitSerializer(data=request.data)
        if business_units.is_valid():
            business_units.save()
            return Response(business_units.data, status=status.HTTP_201_CREATED)
        return Response(business_units.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        business_units = BusinessUnit.objects.all()
        business_units_serializer = BusinessUnitSerializer(business_units, many=True)
        return Response(business_units_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        business_unit = BusinessUnit.objects.get(pk=pk)
        business_unit_serializer = BusinessUnitSerializer(business_unit, data=request.data)
        if business_unit_serializer.is_valid():
            business_unit_serializer.save()
            return Response(business_unit_serializer.data, status=status.HTTP_200_OK)
        return Response(business_unit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        business_unit = BusinessUnit.objects.get(pk=pk)
        business_unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def search(self, request):
        business_units = request.data.get('name')
        if business_units:
            business_units = BusinessUnit.objects.filter(name__icontains=business_units)
            serializer = BusinessUnitSerializer(business_units, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


