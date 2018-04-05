from unittest import skip
from django.test import TestCase
from django.utils.html import escape

from lists.forms import ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List

class MyTest(TestCase):

  def test_invalid_test_items_are_not_saved_in_db(self):

    response = self.client.post(f'/list/new/', data={'text': ''})

    self.assertEqual(List.objects.count(), 0)
    self.assertEqual(Item.objects.count(), 0) 
