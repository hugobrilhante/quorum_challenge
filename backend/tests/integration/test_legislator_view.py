from pathlib import Path

from rest_framework.test import APITestCase

from src.core.models import Legislator
from src.core.serializers import LegislatorSerializer

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / '../../data'


class LegislatorListViewTest(APITestCase):
    def setUp(self):
        self.data = Legislator.data
        self.legislators = Legislator.all()

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
