from rest_framework import viewsets
from management.serializers.profile import ProfileSerializer
from management.models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
