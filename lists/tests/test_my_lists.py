from unittest import skip
from django.test import TestCase
from lists.forms import ItemForm

@skip('Do not wont to test')
class MyTest(TestCase):
  def test_my_tests_for_all(self):
    form = ItemForm()
    self.fail(form.as_p())