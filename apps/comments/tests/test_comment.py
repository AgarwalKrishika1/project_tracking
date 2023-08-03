import json
from apps.base.test_base import BaseTestCase
from rest_framework import status


class CommentTest(BaseTestCase):
    def create_comment(self):
        data = {
            "text": "comment1",
            "created_by": None,
            "comment_issue": None
        }
        response = self.authorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def test_get_comment_authorised(self):
        res = self.create_comment()
        response = self.authorized_pm.get("/comments/")
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
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
        data = {
            "text": "comment1",
            "created_by": None,
            "comment_issue": None
        }
        response = self.unauthorized_pm.post("/comments/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_with_authorised(self):
        res = self.create_comment()
        data = {
            "text": "comment",
            "created_by": None,
            "comment_issue": None
        }
        response = self.authorized_pm.patch(f"/comments/{res.data.get('id')}/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.authorized_pm.get("/comments/")
        self.assertContains(response, '"text":"comment"')

    def test_update_with_unauthorised(self):
        res = self.create_comment()
        data = {
            "text": "comment",
            "created_by": None,
            "comment_issue": None
        }
        response = self.unauthorized_pm.patch(f"/comments/{res.data.get('id')}/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_authorised(self):
        res = self.create_comment()
        response = self.authorized_srd.delete(f"/comments/{res.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_with_unauthorised(self):
        res = self.create_comment()
        url = f"/comments/{res.data.get('id')}/"
        response = self.unauthorized_admin.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

