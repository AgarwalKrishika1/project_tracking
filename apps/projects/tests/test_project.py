import json
from apps.base.test_base import BaseTestCase
from rest_framework import status


class ProjectTestCase(BaseTestCase):
    def create_project(self):
        data = {
            "name": "tests",
            "description": "testing",
        }
        response = self.authorized_pm.post("/clients/projects/", data=data, format='json')
        return response

    def test_get_projects(self):
        res = self.create_project()
        response = self.authorized_pm.get("/clients/projects/")

        # converts byte data string using json.loads()
        data = json.loads(response.content)
        print("Response Data:", data)
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_unauthorised(self):
        res = self.create_project()
        response = self.unauthorized_srd.get("/clients/projects/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_pm(self):
        res = self.create_project()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        response = self.authorized_pm.get("/clients/projects/")
        self.assertContains(response, '"name":"tests"')

    def test_create_with_srd(self):
        data = {
            "name": "tests",
            "description": "testing",
        }
        response = self.authorized_srd.post("/clients/projects/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_pm(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        response = self.authorized_pm.patch("/clients/projects/{}/".format(res.data['id']), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.authorized_pm.get("/clients/projects/")
        self.assertContains(response, '"name":"test123"')

    def test_update_with_jr_developer(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        response = self.authorized_jrd.patch("/clients/projects/{}/".format(res.data['id']), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_unauthorised(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        response = self.unauthorized_pm.patch("/clients/projects/{}/".format(res.data['id']), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_pm(self):
        res = self.create_project()
        response = self.authorized_pm.delete("/clients/projects/{}/".format(res.data['id']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_developer(self):
        res = self.create_project()
        response = self.authorized_srd.delete("/clients/projects/{}/".format(res.data['id']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_project()
        response = self.unauthorized_admin.delete("/clients/projects/{}/".format(res.data['id']))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
