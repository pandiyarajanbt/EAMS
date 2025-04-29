from rest_framework import serializers
from management.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'profile', 'image_capture', 'date', 'check_in', 'check_out', 'current_location', 'is_present']
        