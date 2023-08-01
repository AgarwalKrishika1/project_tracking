import json
from apps.base.test_base import BaseTestCase
from rest_framework import status


class IssueTestCase(BaseTestCase):
    def create_issue(self):
        data = {
            "title": "issue trial",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        response = self.authorized_pm.post("/issues/", data=data, format='json')
        return response

    def test_get_issue(self):
        res = self.create_issue()
        response = self.authorized_pm.get("/issues/")
        data = json.loads(response.content)
        print("Response Data:", data)
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_issue_with_unauthorised(self):
        res = self.create_issue()
        response = self.unauthorized_pm.get("/issues/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_authorised(self):
        res = self.create_issue()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        response = self.authorized_pm.get("/issues/")
        self.assertContains(response, '"title":"issue trial"')

    def test_create_with_unauthorised(self):
        data = {
            "title": "issue trial",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        response = self.unauthorized_pm.post("/issues/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_with_authorised(self):
        res = self.create_issue()
        data = {
            "title": "issue123",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        response = self.authorized_pm.patch(f"/issues/{res.data.get('id')}/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.authorized_pm.get("/issues/")
        self.assertContains(response, '"title":"issue123"')

    def test_update_with_unauthorised(self):
        res = self.create_issue()
        data = {
            "title": "issue123",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        response = self.unauthorized_pm.patch(f"/issues/{res.data.get('id')}/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_authorised(self):
        res = self.create_issue()
        response = self.authorized_srd.delete(f"/issues/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_issue()
        response = self.unauthorized_admin.delete(f"/issues/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class IssueFilterTestCase(IssueTestCase):
    def test_filter_on_type(self):
        res = self.create_issue()
        url = "/issues/" + f"?type=task"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_on_status(self):
        res = self.create_issue()
        url = "/issues/" + f"?status=in_progress"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_on_priority(self):
        res = self.create_issue()
        url = "/issues/" + f"?priority=medium"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_title(self):
        res = self.create_issue()
        url = "/issues/" + f"?title=issue trial"
        response = self.authorized_srd.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_filter_on_title_unauthorised(self):
        res = self.create_issue()
        url = "/issues/" + f"?title=issue trial"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_priority_unauthorised(self):
        res = self.create_issue()
        url = "/issues/" + f"?priority=medium"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_status_unauthorised(self):
        res = self.create_issue()
        url = "/issues/" + f"?status=in_progress"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_filter_on_type_unauthorised(self):
        res = self.create_issue()
        url = "/issues/" + f"?type=task"
        response = self.unauthorized_srd.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
