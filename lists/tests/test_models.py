from django.test import TestCase
from lists.models import List, Item

class ItemAndListModelsTest(TestCase):

    def test_saves_and_retrieves_data_from_db(self):

        lst = List.objects.create()
        Item.objects.create(text='Item one', list=lst)
        Item.objects.create(text='Item two', list=lst)

        saved_items = Item.objects.all()

        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(saved_items[0].text, 'Item one')
        self.assertEqual(saved_items[1].text, 'Item two')

