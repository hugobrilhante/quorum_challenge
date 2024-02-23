from rest_framework.test import APITestCase

from src.core.models import Bill
from src.core.serializers import BillSerializer


class BillListViewTest(APITestCase):
    def setUp(self):
        self.data = Bill.data
        self.bills = Bill.all()

    def test_get_bills(self):
        response = self.client.get('/bills/')

        self.assertEqual(response.status_code, 200)

        data = [
            {
                'id': int(item['id']),
                'title': item['title'],
                'sponsor_id': int(item['sponsor_id']),
            }
            for item in self.data
        ]

        self.assertEqual(response.data, data)

        serializer = BillSerializer(self.bills, many=True)

        self.assertEqual(response.data, serializer.data)
