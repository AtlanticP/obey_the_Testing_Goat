from django.test import TestCase
from lists.models import List, Item
from django.core.exceptions import ValidationError
from unittest import skip

class ItemModelsTest(TestCase):

  def test_cannot_save_an_empty_list_item(self):
    lst = List.objects.create()
    item = Item.objects.create(text='', list=lst)
    with self.assertRaises(ValidationError):
      item.save()
      item.full_clean() 

  def test_duplicate_items_are_invalid(self):
    lst = List.objects.create()
    Item.objects.create(list=lst, text='bla')
    with self.assertRaises(ValidationError):
      item = Item(list=lst, text='bla')
      item.full_clean()
      # item.save() it gives n IntegrityError instead of a ValidationError

  def test_CAN_save_same_item_to_different_lists(self):
    lst1 = List.objects.create()
    lst2 = List.objects.create()
    Item.objects.create(list=lst1, text='bla')
    item = Item(list=lst2, text='bla')
    item.full_clean() # should not raise

  def test_default_text(self):
    item = Item()
    self.assertEqual(item.text, '')

  def test_item_is_related_to_list(self):
    lst = List.objects.create()
    item = Item()
    item.list = lst
    item.save()
    self.assertIn(item, lst.item_set.all())

class ListModelsTest(TestCase):
  def test_get_absolute_url(self):
    lst = List.objects.create()
    self.assertEqual(lst.get_absolute_url(), f'/list/{lst.id}/')
