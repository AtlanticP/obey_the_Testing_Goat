from django.test import TestCase
from lists.models import Item, List

class ListViewTest(TestCase):

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list_field=correct_list)
        Item.objects.create(text='itemey 2', list_field=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list_field=other_list)
        Item.objects.create(text='other list item 2', list_field=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')

        #<h1>Not Found</h1><p>The requested URL /lists1/ was not found on this server.</p>
        # print(response.content.decode())
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 1')

class HomePageTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new/', data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')



class ListAndItemModelsTest(TestCase):

     def test_saving_and_retrieving_items(self):
         list_ = List()
         list_.save()

         first_item = Item()
         first_item.text = 'The first (ever) list item'
         first_item.list_field = list_
         first_item.save()

         second_item = Item()
         second_item.text = 'Item the second'
         second_item.list_field = list_
         second_item.save()

         saved_list = List.objects.first()
         self.assertEqual(saved_list, list_)

         saved_items = Item.objects.all()
         self.assertEqual(saved_items.count(), 2)

         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(first_saved_item.list_field, list_)
         self.assertEqual(second_saved_item.text, 'Item the second')
         self.assertEqual(second_saved_item.list_field, list_)




# class HomePageTest(TestCase):
#     def test_only_saves_items_when_necessary(self):
#         self.client.get('/')
#         self.assertEqual(Item.objects.count(), 0)

    # def test_redirects_after_POST(self):
        # response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    # def test_displays_all_list_items(self):
        # list_ = List.objects.create()
        # Item.objects.create(text='itemey 1', list_field=list_)
        # Item.objects.create(text='itemey 2', list_field=list_)

        # response = self.client.get('/lists/the-only-list-in-the-world/')
        
        # self.assertContains(response, 'itemey 1')
        # self.assertContains(response, 'itemey 2')
    
# class ListViewTest(TestCase):

#     def test_uses_list_template(self):
#         response = self.client.get('/lists/the-only-list-in-the-world/')
#         self.assertTemplateUsed(response, 'list.html')