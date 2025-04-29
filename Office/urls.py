from django.contrib import admin
from django.urls import include, re_path
from management.views.task import TaskView
from management.views.project import ProjectView, BusinessUnitView
from users.views import LoginView, SignUpView, TestTokenView
from management.views.profile import ProfileView
from management.views.attendance import AttendanceView
from management.views.documents_uploads import DocumentsUploadView
urlpatterns = [
    #Admin
    re_path('admin/', admin.site.urls),

    #Auth
    re_path('api/auth/login/', LoginView.as_view(), name='login'),
    re_path('api/auth/signup/', SignUpView.as_view(), name='signup'),
    re_path('api/auth/test-token/', TestTokenView.as_view(), name='test-token'),

    #Task
    re_path('api/task/', TaskView.as_view(), name='create-task'),
    re_path('api/task/update/<int:pk>/', TaskView.as_view(), name='update-task'),
    re_path('api/task/delete/<int:pk>/', TaskView.as_view(), name='delete-task'),
    re_path('api/task/get/<int:pk>/', TaskView.as_view(), name='get-task'),
    re_path('api/task/search/', TaskView.as_view(), name='search-task'),

    #Project
    re_path('api/project/', ProjectView.as_view(), name='create-project'),
    re_path('api/project/update/<int:pk>/', ProjectView.as_view(), name='update-project'),
    re_path('api/project/delete/<int:pk>/', ProjectView.as_view(), name='delete-project'),
    re_path('api/project/get/<int:pk>/', ProjectView.as_view(), name='get-project'),
    re_path('api/project/search/', ProjectView.as_view(), name='search-project'),

    #Profile
    re_path('api/profile/', ProfileView.as_view(), name='create-profile'),
    re_path('api/profile/update/<int:pk>/', ProfileView.as_view(), name='update-profile'),
    re_path('api/profile/delete/<int:pk>/', ProfileView.as_view(), name='delete-profile'),
    re_path('api/profile/get/<int:pk>/', ProfileView.as_view(), name='get-profile'),
    re_path('api/profile/search/', ProfileView.as_view(), name='search-profile'),

    #Business Unit
    re_path('api/business-unit/', BusinessUnitView.as_view(), name='create-business-unit'),
    re_path('api/business-unit/update/<int:pk>/', BusinessUnitView.as_view(), name='update-business-unit'),
    re_path('api/business-unit/delete/<int:pk>/', BusinessUnitView.as_view(), name='delete-business-unit'),
    re_path('api/business-unit/get/<int:pk>/', BusinessUnitView.as_view(), name='get-business-unit'),
    re_path('api/business-unit/search/', BusinessUnitView.as_view(), name='search-business-unit'),

    #Attendance
    re_path('api/attendance/', AttendanceView.as_view(), name='create-attendance'),
    re_path('api/attendance/update/<int:pk>/', AttendanceView.as_view(), name='update-attendance'),
    re_path('api/attendance/get/<int:pk>/', AttendanceView.as_view(), name='get-attendance'),

    #Documents Upload
    re_path('api/documents-upload/', DocumentsUploadView.as_view(), name='create-documents-upload'),
    re_path('api/documents-upload/get', DocumentsUploadView.as_view(), name='get-documents-upload'),
]
