from rest_framework import serializers
from management.models.project import Project, BusinessUnit

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'business_unit',
            'owner',
            'start_date',
            'expected_budget',
            'expected_completion',
            'created_at',
            'updated_at',
        ]

class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = [
            'id',
            'name',
            'description',
        ]
