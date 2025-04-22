from django.urls import path
from management.views.profile import ProfileViewSet

profile_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

profile_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('profile/', profile_list, name='profile-list'),
    path('profile/<int:pk>/', profile_detail, name='profile-detail'),
]

