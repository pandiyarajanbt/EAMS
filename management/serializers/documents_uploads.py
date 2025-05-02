from rest_framework import serializers
from management.models import Documents

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['id', 'profile', 'payslip', 'exp_documents', 'offer_letter', 'pan_card', 'aadhar_card', 'mark_sheet', 'other_documents', 'documents_title']