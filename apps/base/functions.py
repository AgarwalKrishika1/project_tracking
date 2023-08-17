from apps.users.models import UserProfile, User


def create_userprofile(username, email, password, role):
    user = User.objects.create_user(username=username, email=email, password=password)
    user_profile = UserProfile.objects.create(user_id=user.id, role=role)
    return user_profile

