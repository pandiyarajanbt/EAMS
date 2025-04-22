from rest_framework import serializers
from management.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'profile_pic',
            'name',
            'email',
            'phone',
            'address',
            'created_at',
            'updated_at',
        ]
