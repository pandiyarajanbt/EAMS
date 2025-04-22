from django.urls import re_path
from . import views

urlpatterns = [
    re_path('login/', views.LoginView.as_view(), name='login'),
    re_path('signup/', views.SignUpView.as_view(), name='signup'),
    re_path('test-token/', views.TestTokenView.as_view(), name='test-token'),
]
