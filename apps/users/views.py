from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from apps.users.serializer import UserProfileSerializer, UserSerializer
from apps.users.models import UserProfile, User
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserProfileModelView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "first_name": self.request.data.get('first_name'),
                "last_name": self.request.data.get('last_name'),
                "username": self.request.data.get('username'),
            }
        )
        return context


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
