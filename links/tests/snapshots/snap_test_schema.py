# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['LinkTestCase::test_create_link_user_anonymous 1'] = {
    'data': {
        'createLink': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'You must be logged to create link!',
            'path': [
                'createLink'
            ]
        }
    ]
}

snapshots['LinkTestCase::test_create_link_user_logged_in 1'] = {
    'data': {
        'createLink': {
            'description': 'example link',
            'id': 1,
            'url': 'example.com'
        }
    }
}
