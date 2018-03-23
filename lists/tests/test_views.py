from django.test import TestCase
from lists.models import List, Item
from django.utils.html import escape

class HomePageTest(TestCase):

    def test_uses_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ListView(TestCase):

    def test_uses_list_template(self):

        lst = List.objects.create()
        response = self.client.get(f'/list/{lst.id}/')
        
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_items_from_correct_list(self):
       
       correct_list = List.objects.create()
       other_list = List.objects.create()
       Item.objects.create(text='Item one', list=correct_list)
       Item.objects.create(text='Item two', list=correct_list)    

       response = self.client.get(f'/list/{correct_list.id}/')

       self.assertContains(response, 'Item one')
       self.assertContains(response, 'Item two')
        
class AddItemTest(TestCase):

    def test_can_save_a_POST_request(self):

       lst = List.objects.create()        
       response = self.client.post(f'/list/{lst.id}/add_item/', data={'item_text': 'A new list item'})

       self.assertEqual(Item.objects.count(), 1)

       item = Item.objects.first()
       self.assertIn('new', item.text)

    def test_redirects_after_post_request_adding_item(self):
       lst = List.objects.create()
       response = self.client.post(f'/list/{lst.id}/add_item/', data={'item_text': 'A new list item'})
       
       self.assertRedirects(response, f'/list/{lst.id}/')


class NewItemTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/list/new/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertIn('A new list item', new_item.text)
        self.assertRedirects(response, f'/list/{new_item.id}/')

    def test_redirects_to_list_view(self):
        response = self.client.post('/list/new/', data={'item_text': 'A new list item'})

        lst = List.objects.first()

        self.assertRedirects(response, f'/list/{lst.id}/')


class NewListTest(TestCase):

  def test_validation_errors_are_sent_back_to_home_page_template(self):

    response = self.client.post(f'/list/new/', data={'item_text': ''})

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')

    expected_error = escape("You can't have an empty list item")
    self.assertContains(response, expected_error)
      

  def test_invalid_test_items_are_not_saved_in_db(self):

    response = self.client.post(f'/list/new/', data={'item_text': ''})

    self.assertEqual(List.objects.count(), 0)
    self.assertEqual(Item.objects.count(), 0)    
        