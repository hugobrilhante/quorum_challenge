from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from src.core.models import Bill
from src.core.models import Legislator
from src.core.models import Vote


class BillDetailsViewTest(APITestCase):
    def setUp(self):
        self.bill = Bill.get(id=2952375)
        self.legislator = Legislator.get(id=self.bill.sponsor_id)
        self.vote = Vote.get(bill_id=self.bill.id)

    def test_get_bill_details(self):
        url = reverse('bill-details', kwargs={'bill_id': self.bill.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.bill.id)
        self.assertEqual(response.data['title'], self.bill.title)
        self.assertEqual(response.data['supporters'], 6)
        self.assertEqual(response.data['opposers'], 13)
        self.assertEqual(response.data['sponsor'], self.legislator.name)

    def test_invalid_bill_id(self):
        url = reverse('bill-details', kwargs={'bill_id': 999})  # Non-existing bill id
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_no_sponsor(self):
        self.bill = Bill.get(id=2900994)
        url = reverse('bill-details', kwargs={'bill_id': self.bill.id})
        response = self.client.get(url)
        self.assertIsNone(response.data['sponsor'])
