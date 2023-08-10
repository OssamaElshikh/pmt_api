from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class ProfileListAPIView(ListCreateAPIView):
    """
    List/Create profiles 
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update/Delete a profile 
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# user authentication part:


class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Register a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# UserObtainTokenView
# class UserObtainTokenView(generics.CreateAPIView):
#     """
#     Obtain JWT token for user authentication.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = User.objects.filter(username=username).first()
#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             user_data = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return Response(user_data, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
