from django.urls import path
from management.views.profile import ProfileViewSet
from management.views.task import CreateTaskView, UpdateTaskView, DeleteTaskView, GetTaskView

urlpatterns = [
    path('task/', CreateTaskView.as_view(), name='create-task'),
    path('task/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    path('task/<int:pk>/', GetTaskView.as_view(), name='get-task'),
]

