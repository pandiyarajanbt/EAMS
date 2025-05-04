from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Token based authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            user = User.objects.get(username=username)
            
            # Check if user is staff or superuser, they should use different login endpoints
            if user.is_staff or user.is_superuser:
                return Response({"message": "Please use the appropriate staff or admin login"}, 
                                status=status.HTTP_403_FORBIDDEN)
                
            if not user.check_password(password):
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
                
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class StaffLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            staff_user = User.objects.get(username=username, is_staff=True)
            
            if not staff_user.check_password(password):
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
                
            token, created = Token.objects.get_or_create(user=staff_user)
            return Response({
                "token": token.key,
                "user": UserSerializer(staff_user).data
            }, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
class AdminLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            admin_users = User.objects.get(username=username, is_superuser=True)

            if not admin_users.check_password(password):  # Fixed: using actual password instead of hardcoded 'password'
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            token, created = Token.objects.get_or_create(user=admin_users)
            return Response({
                "token": token.key,
                "user": UserSerializer(admin_users).data
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:  # Fixed: catching specific exception
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TestTokenView(APIView):
    def get(self, request):
        data  =  {
            'username': request.user.username,
            'email': request.user.email,
            'token': request.auth.key
        }
        return Response(data)



