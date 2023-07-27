from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.viewsets import ModelViewSet
from apps.users.serializer import UserProfileSerializer, UserSerializer
from apps.users.models import UserProfile, User
from rest_framework.permissions import IsAuthenticated, BasePermission


# Create your views here.

class IsAuthenticatedOrPostOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow unauthenticated access for POST requests
        if request.method == 'POST':
            return True
        # Authenticate other requests using IsAuthenticated
        return IsAuthenticated().has_permission(request, view)


class UserProfileModelView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrPostOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "first_name": self.request.data.get('first_name'),
                "last_name": self.request.data.get('last_name'),
                "username": self.request.data.get('username'),
                "password": self.request.data.get('password'),
                "email": self.request.data.get('email')
            }
        )
        return context


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
