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
        data_json = json.dumps(data)
        response = self.authorized_pm.post("/clients/project/", data=data_json, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def test_get_projects(self):
        res = self.create_project()
        response = self.authorized_pm.get("/clients/project/")
        # converts byte data string using json.loads()
        data = json.loads(response.content)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_unauthorised(self):
        res = self.create_project()
        response = self.unauthorized_srd.get("/clients/project/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_pm(self):
        res = self.create_project()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        response = self.authorized_pm.get("/clients/project/")
        self.assertContains(response, '"name":"tests"')

    def test_create_with_srd(self):
        data = {
            "name": "tests",
            "description": "testing",
        }
        data_json = json.dumps(data)
        response = self.authorized_srd.post("/clients/project/", data=data_json, content_type='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_pm(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
            "status": "ACTIVE",
        }
        data_json = json.dumps(data)
        response = self.authorized_pm.patch(f"/clients/project/{res.data.get('id')}/", data=data_json,
                                            content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '"name":"test123"')

    def test_update_with_jr_developer(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        data_json = json.dumps(data)
        response = self.authorized_jrd.patch(f"/clients/project/{res.data.get('id')}/", data=data_json,
                                             content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_unauthorised(self):
        res = self.create_project()
        data = {
            "name": "test123",
            "description": "testing",
        }
        data_json = json.dumps(data)
        response = self.unauthorized_pm.patch(f"/clients/project/{res.data.get('id')}/", data=data_json,
                                              content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_pm(self):
        res = self.create_project()
        response = self.authorized_pm.delete(f"/clients/project/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_developer(self):
        res = self.create_project()
        response = self.authorized_srd.delete(f"/clients/project/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_project()
        response = self.unauthorized_admin.delete(f"/clients/project/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProjectFilterTestCase(ProjectTestCase):
    def test_filter_on_status(self):
        self.test_update_with_pm()
        url = "/clients/project/" + f"?status=ACTIVE"
        response = self.authorized_srd.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_on_pm(self):
        self.test_update_with_pm()
        url = "/clients/project/" + f"?project_manager={self.project_manager_userprofile.id}"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_name(self):
        res = self.create_project()
        url = "/clients/project/" + f"?name=tests"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_name_unauthorised(self):
        res = self.create_project()
        url = "/clients/project/" + f"?name=tests"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_pm_unauthorised(self):
        res = self.create_project()
        url = "/clients/project/" + f"?project_manager={self.project_manager_userprofile.id}"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_status_unauthorised(self):
        res = self.create_project()
        url = "/clients/project/" + f"?status=ACTIVE"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

