from rest_framework.test import APITestCase

from src.core.models import Bill
from src.core.serializers import BillSerializer


class BillListViewTest(APITestCase):
    def setUp(self):
        self.bills = []
        for i in range(1, 4):
            bill = Bill(id=i, title=f'Bill {i}', sponsor_id=i)
            self.bills.append(bill)

    def test_get_bills(self):
        response = self.client.get('/bills/')

        self.assertEqual(response.status_code, 200)

        expected_data = [
            {'id': 1, 'title': 'Bill 1', 'sponsor_id': 1},
            {'id': 2, 'title': 'Bill 2', 'sponsor_id': 2},
            {'id': 3, 'title': 'Bill 3', 'sponsor_id': 3},
        ]
        self.assertEqual(response.data, expected_data)

        serializer = BillSerializer(self.bills, many=True)
        self.assertEqual(response.data, serializer.data)
