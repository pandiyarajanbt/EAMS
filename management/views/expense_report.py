from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from management.models import ExpenseReport, ExpenseReportApproval, ExpenseReportProcess
from management.serializers import ExpenseReportSerializers, ExpenseReportApprovalSerializers, ExpenseReportProcessSerializers

# apis

class ExpenseReportApiView(APIView):
    def post(self, request):
        serializer = ExpenseReportSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        expenses_data = ExpenseReport.objects.all()
        serializer = ExpenseReportSerializers(expenses_data, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return []