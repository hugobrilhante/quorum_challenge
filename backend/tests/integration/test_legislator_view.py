from rest_framework.test import APITestCase

from src.core.models import Legislator
from src.core.serializers import LegislatorSerializer


class LegislatorListViewTest(APITestCase):
    def setUp(self):
        self.legislators = []
        for i in range(1, 4):
            legislator = Legislator(id=i, name=f'Legislator {i}')
            self.legislators.append(legislator)

    def test_get_legislators(self):
        response = self.client.get('/legislators/')

        self.assertEqual(response.status_code, 200)

        expected_data = [
            {'id': 1, 'name': 'Legislator 1'},
            {'id': 2, 'name': 'Legislator 2'},
            {'id': 3, 'name': 'Legislator 3'},
        ]
        self.assertEqual(response.data, expected_data)

        serializer = LegislatorSerializer(self.legislators, many=True)
        self.assertEqual(response.data, serializer.data)
