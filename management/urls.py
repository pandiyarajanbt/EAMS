from django.urls import path
from management.views.task import TaskView
from management.views.project import ProjectView

urlpatterns = [
    path('task/', TaskView.as_view(), name='create-task'),
    path('task/update/<int:pk>/', TaskView.as_view(), name='update-task'),
    path('task/delete/<int:pk>/', TaskView.as_view(), name='delete-task'),
    path('task/get/<int:pk>/', TaskView.as_view(), name='get-task'),
    path('task/search/', TaskView.as_view(), name='search-task'),
    path('project/', ProjectView.as_view(), name='create-project'),
    path('project/update/<int:pk>/', ProjectView.as_view(), name='update-project'),
    path('project/delete/<int:pk>/', ProjectView.as_view(), name='delete-project'),
    path('project/get/<int:pk>/', ProjectView.as_view(), name='get-project'),
    path('project/search/', ProjectView.as_view(), name='search-project'),
]

