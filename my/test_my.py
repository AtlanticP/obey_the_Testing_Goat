from unittest import skip
from django.test import TestCase
from django.utils.html import escape

from lists.forms import ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List

class MyTest(TestCase):
  
  @skip('my developed test')
  def test_displays_item_form(self):
    lst = List.objects.create()
    response = self.client.get(f'/lists/{lst.id}/')
    self.assertIsInstance(response.context['form'], ExistingListItemForm)
    self.assertContains(response, 'name="text"')
