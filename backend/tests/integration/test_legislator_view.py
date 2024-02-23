import os
from pathlib import Path

from rest_framework.test import APITestCase

from src.core.models import Legislator
from src.core.parsers import CSVParser
from src.core.serializers import LegislatorSerializer

BASE_DIR = Path(__file__).resolve().parent


class LegislatorListViewTest(APITestCase):
    def setUp(self):
        self.data = CSVParser(os.path.join(BASE_DIR, '../../src/core/data/legislators.csv')).get_data()
        self.legislators = [Legislator(**legislator) for legislator in self.data]

    def test_get_legislators(self):
        response = self.client.get('/legislators/')

        self.assertEqual(response.status_code, 200)

        data = [
            {
                'id': int(item['id']),
                'name': item['name'],
            }
            for item in self.data
        ]

        self.assertEqual(response.data, data)

        serializer = LegislatorSerializer(self.legislators, many=True)

        self.assertEqual(response.data, serializer.data)
