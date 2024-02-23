from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from src.core.models import Legislator


class LegislatorDetailViewTest(APITestCase):
    def setUp(self):
        self.legislator = Legislator.get(id=904789)

    def test_get_legislator_detail(self):
        url = reverse('legislator-detail', kwargs={'legislator_id': self.legislator.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.legislator.id)
        self.assertEqual(response.data['name'], self.legislator.name)
        self.assertEqual(response.data['supported'], 1)
        self.assertEqual(response.data['opposed'], 1)

    def test_get_legislator_detail_not_found(self):
        url = reverse('legislator-detail', kwargs={'legislator_id': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
