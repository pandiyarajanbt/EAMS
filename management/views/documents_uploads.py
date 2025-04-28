from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from management.serializers import DocumentsSerializer
from management.models import Documents


class DocumentsUploadView(APIView):
    def post(self, request):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        documents = Documents.objects.all()
        serializer = DocumentsSerializer(documents, many=True)
        return Response(serializer.data)
    
    