import json
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from apps.base.functions import create_userprofile
from apps.base.test_base import BaseTestCase
from rest_framework import status
from apps.issues.models import Issues

USER = "user "
PASSWORD = "1234"
EMAIL = "testuser@gmail.com"


class CommentTest(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super(BaseTestCase, cls).setUpTestData()
        user = create_userprofile(username=USER, email=EMAIL, password=PASSWORD,
                                  role="project_manager")
        cls.user_userprofile = user

    def setUp(self) -> None:
        issue_data = {
            "title": "issue trial",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        self.issue = Issues.objects.create(**issue_data)

        super(BaseTestCase, self).setUp()
        self.project_manager = User.objects.filter(username=USER).first()
        pm_token = RefreshToken.for_user(self.project_manager)
        pm_access_key = str(pm_token.access_token)
        self.unauthorized_pm = APIClient(self.project_manager)
        self.authorized_pm = APIClient(self.project_manager)
        self.authorized_pm.credentials(HTTP_AUTHORIZATION="Bearer " + pm_access_key)

    def create_comment(self):
        data = {
            "text": "comment1",
            "created_by": self.user_userprofile.id,
            "issue": self.issue.id
        }
        response = self.authorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def create_comment_with_unauthorised(self):
        data = {
            "text": "comment1",
            "created_by": self.user_userprofile.id,
            "issue": self.issue.id
        }
        response = self.unauthorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        return response

    def update_comment_with_authorised(self):
        data = {
            "text": "comment1",
            "created_by": self.user_userprofile.id,
            "issue": self.issue.id
        }
        response = self.authorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def update_comment_with_unauthorised(self):
        data = {
            "text": "comment1",
            "created_by": self.user_userprofile.id,
            "issue": self.issue.id
        }
        response = self.unauthorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        return response

    def test_get_comment_authorised(self):
        res = self.create_comment()
        response = self.authorized_pm.get("/comments/")
        data = json.loads(response.content)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comment_with_unauthorised(self):
        res = self.create_comment()
        response = self.unauthorized_pm.get("/comments/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_authorised(self):
        res = self.create_comment()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        response = self.authorized_pm.get("/comments/")
        self.assertContains(response, '"text":"comment1"')

    def test_create_with_unauthorised(self):
        res = self.create_comment_with_unauthorised()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_with_authorised(self):
        res = self.update_comment_with_authorised()
        response = self.authorized_pm.patch(f"/comments/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '"text":"comment1"')

    def test_update_with_unauthorised(self):
        res = self.update_comment_with_unauthorised()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_authorised(self):
        res = self.create_comment()
        response = self.authorized_pm.delete(f"/comments/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_comment()
        url = f"/comments/{res.data.get('id')}/"
        response = self.unauthorized_pm.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestCommentFilter(CommentTest):
    def test_filter_on_text(self):
        res = self.create_comment()
        url = "/comments/" + f"?text=comment1"
        response = self.authorized_pm.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_text_unauthorised(self):
        res = self.create_comment()
        url = "/comments/" + f"?text=comment1"
        response = self.unauthorized_pm.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_created_by(self):
        res = self.create_comment()
        url = "/comments/" + f"?created_by={self.user_userprofile.id}"
        response = self.authorized_pm.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_created_by_unauthorised(self):
        res = self.create_comment()
        url = "/comments/" + f"?created_by={self.user_userprofile.id}"
        response = self.unauthorized_pm.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)