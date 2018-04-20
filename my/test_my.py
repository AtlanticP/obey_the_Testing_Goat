from unittest import skip
from django.test import TestCase
from django.utils.html import escape

from lists.forms import ItemForm, EMPTY_ITEM_ERROR
from lists.models import Item, List

class MyTest(TestCase):
  
  @skip('my developed test')
  def test_my(self):
    response = self.client.get("/static/somefile.json")


