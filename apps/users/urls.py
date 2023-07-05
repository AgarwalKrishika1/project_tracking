from django.urls import path, include
from apps.users.views import UserCreate
from apps.users.views import UserProfileModelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserProfileModelView, basename='user'),
router.register(r'create', UserCreate, basename='craete')

#
# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls
