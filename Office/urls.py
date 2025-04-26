from django.contrib import admin
from django.urls import include, re_path
from management.views.task import TaskView
from management.views.project import ProjectView, BusinessUnitView
from users.views import LoginView, SignUpView, TestTokenView
from management.views.profile import ProfileView

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/auth/login/', LoginView.as_view(), name='login'),
    re_path('api/auth/signup/', SignUpView.as_view(), name='signup'),
    re_path('api/auth/test-token/', TestTokenView.as_view(), name='test-token'),
    re_path('api/task/', TaskView.as_view(), name='create-task'),
    re_path('api/task/update/<int:pk>/', TaskView.as_view(), name='update-task'),
    re_path('api/task/delete/<int:pk>/', TaskView.as_view(), name='delete-task'),
    re_path('api/task/get/<int:pk>/', TaskView.as_view(), name='get-task'),
    re_path('api/task/search/', TaskView.as_view(), name='search-task'),
    re_path('api/project/', ProjectView.as_view(), name='create-project'),
    re_path('api/project/update/<int:pk>/', ProjectView.as_view(), name='update-project'),
    re_path('api/project/delete/<int:pk>/', ProjectView.as_view(), name='delete-project'),
    re_path('api/project/get/<int:pk>/', ProjectView.as_view(), name='get-project'),
    re_path('api/project/search/', ProjectView.as_view(), name='search-project'),
    re_path('api/profile/', ProfileView.as_view(), name='create-profile'),
    re_path('api/profile/update/<int:pk>/', ProfileView.as_view(), name='update-profile'),
    re_path('api/profile/delete/<int:pk>/', ProfileView.as_view(), name='delete-profile'),
    re_path('api/profile/get/<int:pk>/', ProfileView.as_view(), name='get-profile'),
    re_path('api/profile/search/', ProfileView.as_view(), name='search-profile'),
    re_path('api/business-unit/', BusinessUnitView.as_view(), name='create-business-unit'),
    re_path('api/business-unit/update/<int:pk>/', BusinessUnitView.as_view(), name='update-business-unit'),
    re_path('api/business-unit/delete/<int:pk>/', BusinessUnitView.as_view(), name='delete-business-unit'),
    re_path('api/business-unit/get/<int:pk>/', BusinessUnitView.as_view(), name='get-business-unit'),
    re_path('api/business-unit/search/', BusinessUnitView.as_view(), name='search-business-unit'),
]
