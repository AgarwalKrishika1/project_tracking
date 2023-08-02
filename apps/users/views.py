from rest_framework.viewsets import ModelViewSet
from apps.users.serializer import UserProfileSerializer
from apps.users.models import UserProfile
from apps.base.permissions import IsAuthenticatedOrPostOnly


class UserProfileViewSet(ModelViewSet):
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
