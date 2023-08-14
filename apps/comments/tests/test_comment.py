import json
from apps.base.test_base import BaseTestCase
from rest_framework import status
from apps.issues.models import Issue

USER = "user "
PASSWORD = "1234"
EMAIL = "testuser@gmail.com"


class CommentTest(BaseTestCase):

    def setUp(self):
        super(CommentTest, self).setUp()
        issue_data = {
            "title": "issue trial",
            "description": "issues trial",
            "type": "task",
            "status": "in_progress",
            "priority": "medium"
        }
        self.issue = Issue.objects.create(**issue_data)

    def create_comment(self):
        data = {
            "text": "comment1",
            "created_by": self.project_manager_userprofile.id,
            "issue": self.issue.id
        }
        data_json = json.dumps(data)
        response = self.authorized_pm.post("/comments/", data=data_json, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def create_comment_with_unauthorised(self):
        data = {
            "text": "comment1",
            "created_by": self.project_manager_userprofile.id,
            "issue": self.issue.id
        }
        data_json = json.dumps(data)
        response = self.unauthorized_pm.post("/comments/", data=data_json, content_type="application/json")
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

    def test_create_with_unauthorised(self):
        res = self.create_comment_with_unauthorised()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_with_authorised(self):
        res = self.create_comment()
        data = {
            "text": "comment1",
            "created_by": self.project_manager_userprofile.id,
            "issue": self.issue.id
        }
        data_json = json.dumps(data)
        response = self.authorized_pm.patch(f"/comments/{res.data.get('id')}/", data=data_json,
                                            content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '"text":"comment1"')

    def test_update_with_unauthorised(self):
        res = self.create_comment()
        data = {
            "text": "comment1",
            "created_by": self.project_manager_userprofile.id,
            "issue": self.issue.id
        }
        data_json = json.dumps(data)
        response = self.unauthorized_pm.patch(f"/comments/{res.data.get('id')}/", data=data_json,
                                              content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

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
        url = f"/comments/?text=comment1"
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
        url = "/comments/" + f"?created_by={self.project_manager_userprofile.id}"
        response = self.authorized_pm.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_created_by_unauthorised(self):
        res = self.create_comment()
        url = "/comments/" + f"?created_by={self.project_manager_userprofile.id}"
        response = self.unauthorized_pm.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
