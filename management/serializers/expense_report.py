from rest_framework import serializers
from management.models.expense import ExpenseReport, ExpenseReportApproval, ExpenseReportProcess


class ExpenseReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExpenseReport
        fields = '__all__'


class ExpenseReportApprovalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExpenseReportApproval
        fields = '__all__'


class ExpenseReportProcessSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExpenseReportProcess
        fields = '__all__'