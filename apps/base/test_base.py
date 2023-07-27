from django.urls import reverse

from apps.base.functions import create_userprofile
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import UserProfile,User

ADMIN_USER = "admin"
ADMIN_PASSWORD = "1234"
ADMIN_EMAIL = "admin@gmail.com"

PM_USER = "test pm"
PM_PASSWORD = "1234"
PM_EMAIL = "testpm@gmail.com"

SR_DEVELOPER_USER = "test sr developer"
SR_DEVELOPER_PASSWORD = "1234"
SR_DEVELOPER_EMAIL = "testsr@gmail.com"

JR_DEVELOPER_USER = "test jr developer"
JR_DEVELOPER_PASSWORD = "1234"
JR_DEVELOPER_EMAIL = "testjr@gmail.com"


class BaseTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        super(BaseTestCase, cls).setUpTestData()
        project_manager = create_userprofile(username=PM_USER, email=PM_EMAIL, password=PM_PASSWORD, role="project_manager")
        admin = User.objects.create_superuser(username=ADMIN_USER, email=ADMIN_EMAIL, password=ADMIN_PASSWORD)
        sr_developer = create_userprofile(username=SR_DEVELOPER_USER, email=SR_DEVELOPER_EMAIL, password=SR_DEVELOPER_PASSWORD, role="sr_developer")
        jr_developer = create_userprofile(username=JR_DEVELOPER_USER, email=JR_DEVELOPER_EMAIL, password=JR_DEVELOPER_PASSWORD, role="jr_developer")
    def setUp(self) -> None:
        super(BaseTestCase, self).setUp()
        self.user = get_user_model().objects.filter(username="admin").first()
        self.project_manager = UserProfile.objects.filter(user__username=PM_USER).first()
        self.sr_developer = UserProfile.objects.filter(user__username=SR_DEVELOPER_USER).first()
        self.jr_developer = UserProfile.objects.filter(user__username=JR_DEVELOPER_USER).first()
        user_token = RefreshToken.for_user(self.user)
        user_access_key = str(user_token.access_token)
        pm_token = RefreshToken.for_user(self.project_manager)
        pm_access_key = str(pm_token.access_token)
        sr_developer_token = RefreshToken.for_user(self.sr_developer)
        sr_developer_access_key = str(sr_developer_token.access_token)
        jr_developer_token = RefreshToken.for_user(self.jr_developer)
        jr_developer_access_key = str(jr_developer_token.access_token)
        self.unauthorized_pm = APIClient(self.project_manager)
        self.authorized_pm = APIClient(self.project_manager)
        self.authorized_pm.credentials(HTTP_AUTHORIZATION="Bearer " + pm_access_key)

        self.unauthorized_client = APIClient(self.user)
        self.authorized_client = APIClient(self.user)
        self.authorized_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_access_key)

        self.unauthorized_srd = APIClient(self.sr_developer)
        self.authorized_srd = APIClient(self.sr_developer)
        self.authorized_srd.credentials(HTTP_AUTHORIZATION="Bearer " + sr_developer_access_key)

        self.unauthorized_jrd = APIClient(self.jr_developer)
        self.authorized_jrd = APIClient(self.jr_developer)
        self.authorized_jrd.credentials(HTTP_AUTHORIZATION="Bearer " + jr_developer_access_key)

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
