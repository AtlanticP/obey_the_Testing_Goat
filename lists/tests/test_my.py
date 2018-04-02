from django.test import TestCase
from unittest import skip

from lists.forms import ItemForm

@skip
class MyTest(TestCase):
  def test_my(self):
    self.fail(ItemForm().as_p())