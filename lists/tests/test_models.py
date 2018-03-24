from django.test import TestCase
from lists.models import List, Item
from django.core.exceptions import ValidationError

class ItemAndListModelsTest(TestCase):

    def test_saves_and_retrieves_data_from_db(self):

        lst = List.objects.create()
        Item.objects.create(text='Item one', list=lst)
        Item.objects.create(text='Item two', list=lst)

        saved_items = Item.objects.all()

        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(saved_items[0].text, 'Item one')
        self.assertEqual(saved_items[1].text, 'Item two')

    def test_cannot_save_an_empty_list_item(self):

        lst = List.objects.create()
        item = Item.objects.create(text='', list=lst)

        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
        lst = List.objects.create()
        self.assertEqual(lst.get_absolute_url(), f'/list/{lst.id}/')