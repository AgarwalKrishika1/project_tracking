import json

from apps.base.test_base import BaseTestCase
from apps.users.models import UserProfile
from apps.projects.models import Projects
from rest_framework import status
from apps.base.functions import create_userprofile


class ProjectTestCase(BaseTestCase):
    def create_project(self):
        data = {
            "name": "test",
            "description": "testing",
        }
        response = self.authorized_pm.post("/clients/projects/", data=data, format='json')
        return response

    def test_get_projects(self):
        res = self.create_project()
        response = self.authorized_pm.get("/clients/projects/")
        self.assertContains(response, "test")
        self.assertContains(response, "testing")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # converts byte data string using json.loads()
        data = json.loads(response.content)

        print("Response Data:", data)
