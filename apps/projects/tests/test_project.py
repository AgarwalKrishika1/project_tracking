import json
from apps.base.test_base import BaseTestCase
from rest_framework import status


class ProjectTestCase(BaseTestCase):
    def create_project(self):
        data = {
            "name": "tests",
            "description": "testing",
            "project_manager": self.project_manager_userprofile.id
        }
        response = self.authorized_pm.post("/clients/projects/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def test_get_projects(self):
        res = self.create_project()
        response = self.authorized_pm.get("/clients/projects/")

        # converts byte data string using json.loads()
        data = json.loads(response.content)
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
            "status": "ACTIVE",
        }
        response = self.authorized_pm.patch(f"/clients/projects/{res.data.get('id')}/", data=data,
                                            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.authorized_pm.get("/clients/projects/")
        self.assertContains(response, '"name":"test123"')

    def test_update_with_jr_developer(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        response = self.authorized_jrd.patch(f"/clients/projects/{res.data.get('id')}/", data=data,
                                             format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_unauthorised(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        response = self.unauthorized_pm.patch(f"/clients/projects/{res.data.get('id')}/", data=data,
                                              format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_pm(self):
        res = self.create_project()
        response = self.authorized_pm.delete(f"/clients/projects/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_developer(self):
        res = self.create_project()
        response = self.authorized_srd.delete(f"/clients/projects/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_project()
        response = self.unauthorized_admin.delete(f"/clients/projects/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProjectFilterTestCase(ProjectTestCase):
    def test_filter_on_status(self):
        self.test_update_with_pm()
        url = "/clients/projects/" + f"?status=ACTIVE"
        response = self.authorized_srd.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_on_pm(self):
        self.test_update_with_pm()
        url = "/clients/projects/" + f"?project_manager={self.project_manager_userprofile.id}"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_name(self):
        res = self.create_project()
        url = "/clients/projects/" + f"?name=tests"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_name_unauthorised(self):
        res = self.create_project()
        url = "/clients/projects/" + f"?name=tests"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_pm_unauthorised(self):
        res = self.create_project()
        url = "/clients/projects/" + f"?project_manager={self.project_manager_userprofile.id}"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_status_unauthorised(self):
        res = self.create_project()
        url = "/clients/projects/" + f"?status=ACTIVE"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

