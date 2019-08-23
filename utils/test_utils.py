from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from snapshottest.django import TestCase
from graphene.test import Client

from hackernews.schema import schema


class APITestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client(schema)

    def snapshot_graphql_request(
            self,
            request_string,
            context=None,
            variables=None
    ):
        if context is None:
            context = {}
        graphql_response = self.client.execute(
            request_string,
            variables=variables,
            context=self.generate_context(**context)
        )
        self.assertMatchSnapshot(graphql_response)

    def generate_context(self, user=None, files=None):
        request = RequestFactory()
        context_value = request.get('/graphql/')
        context_value.user = user or AnonymousUser()
        self.__set_context_files(context_value, files)
        return context_value

    @staticmethod
    def __set_context_files(context, files):
        if isinstance(files, dict):
            for name, file in files.items():
                context.FILES[name] = file
