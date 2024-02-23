from unittest.mock import mock_open
from unittest.mock import patch

from django.test import TestCase

from src.core.parsers import CSVParser


class TestCSVParser(TestCase):
    def setUp(self):
        self.csv_data = (
            'id,name\n'
            '904789,Rep. Don Bacon (R-NE-2)\n'
            '1603850,Rep. Jamaal Bowman (D-NY-16)\n'
            '1852382,Rep. Cori Bush (D-MO-1)\n'
        )
        self.expected_data = [
            {'id': '904789', 'name': 'Rep. Don Bacon (R-NE-2)'},
            {'id': '1603850', 'name': 'Rep. Jamaal Bowman (D-NY-16)'},
            {'id': '1852382', 'name': 'Rep. Cori Bush (D-MO-1)'},
        ]

    def test_load_data(self):
        with patch('builtins.open', mock_open(read_data=self.csv_data)):
            parser = CSVParser('dummy_path.csv')
            data = parser.load_data()
            self.assertEqual(data, self.expected_data)
