# user_auth/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from api_services.serialazer.UserAuthSerializer import UserRegistrationSerializer
from drf_yasg.utils import swagger_auto_schema
# Registration View
class UserRegistrationView(APIView):
    permission_classes = () # Allow any user to access this endpoint
    
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer, # This is the key change
        operation_description="Register a new user, requires username, email, password, and password2.",
        responses={201: 'User created successfully', 400: 'Invalid input'}
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Optional: Auto-create a token upon registration
            # from rest_framework.authtoken.models import Token
            # token = Token.objects.get(user=user)
            return Response({
                "message": "User registered successfully",
                # "token": token.key # Include token if auto-generating
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View (Uses DRF's built-in token-obtaining logic)
# It expects 'username' and 'password' in the request and returns a 'token'.
# You can use rest_framework.authtoken.views.obtain_auth_token directly in urls.py