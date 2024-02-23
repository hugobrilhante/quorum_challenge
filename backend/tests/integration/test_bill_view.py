from rest_framework.test import APITestCase

from src.core.models import Bill
from src.core.serializers import BillSerializer


class BillListViewTest(APITestCase):
    def setUp(self):
        self.bills = Bill.all()

    def test_get_bills(self):
        response = self.client.get('/bills/')

        self.assertEqual(response.status_code, 200)

        serializer = BillSerializer(self.bills, many=True)

        self.assertEqual(response.data, serializer.data)
