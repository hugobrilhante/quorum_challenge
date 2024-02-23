from django.test import TestCase

from src.core.data_sourcers import DataSource
from src.core.models import BaseModel

NAME_1 = 'Test 1'
NAME_2 = 'Test 2'


class DataSourceTest(DataSource):
    def get_data(self):
        return [
            {'id': '1', 'name': NAME_1},
            {'id': '2', 'name': NAME_2},
        ]


class ModelTest(BaseModel):
    data_source = DataSourceTest


class BaseModelTestCase(TestCase):
    def setUp(self):
        self.test_data = DataSourceTest().get_data()

    def test_all(self):
        instances = ModelTest.all()
        self.assertEqual(len(instances), len(self.test_data))
        for instance, data in zip(instances, self.test_data):
            self.assertEqual(instance.id, data['id'])
            self.assertEqual(instance.name, data['name'])

    def test_get_single_item(self):
        item = ModelTest.get(id=1)
        self.assertEqual(item.id, '1')
        self.assertEqual(item.name, NAME_1)

    def test_get_multiple_items(self):
        with self.assertRaises(ValueError):
            ModelTest.get(name='Teste')

    def test_get_item_not_found(self):
        with self.assertRaises(ValueError):
            ModelTest.get(id=100)

    def test_filter(self):
        filtered_items = ModelTest.filter(name=NAME_1)
        self.assertEqual(len(filtered_items), 1)
        self.assertEqual(filtered_items[0].id, '1')
        self.assertEqual(filtered_items[0].name, NAME_1)

    def test_matches_filters(self):
        instance = ModelTest.get(id=1)
        self.assertTrue(ModelTest._matches_filters(instance, {'id': '1', 'name': NAME_1}))
        self.assertFalse(ModelTest._matches_filters(instance, {'id': '2', 'name': NAME_2}))
