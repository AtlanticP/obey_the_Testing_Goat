from django.test import TestCase
from lists.models import Item

class HomePageTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

class ItemModelTest(TestCase):

    def test_retrieves_and_saves_items(self):
        
        first_item = Item()
        first_item.text = 'item one' 
        first_item.save()

        second_item = Item()
        second_item.text = 'item two'
        second_item.save()

        items_saved = Item.objects.all()
        self.assertEqual(items_saved.count(), 2)

        first_item_text = items_saved[0].text
        second_item_text = items_saved[1].text

        self.assertIn('one', first_item_text)
        self.assertIn('two', second_item_text)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')