from django.contrib.auth import get_user_model
from utils.test_utils import APITestCase
from .graphql_requests import (
    CREATE_LINK_MUTATION
)


class LinkTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.dummy_user = get_user_model().objects.create(
            username="dummy_user",
            password="dummy_password"
        )

    def test_create_link_user_anonymous(self):
        self.snapshot_graphql_request(
            request_string=CREATE_LINK_MUTATION,
            variables={"url": "example.com", "desc": "example link"},
        )

    def test_create_link_user_logged_in(self):
        self.snapshot_graphql_request(
            request_string=CREATE_LINK_MUTATION,
            variables={"url": "example.com", "desc": "example link"},
            context={
                "user": self.dummy_user,
            }
        )
