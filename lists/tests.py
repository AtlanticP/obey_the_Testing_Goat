from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import List, Item
from django.utils.html import escape
from lists.forms import ItemForm, EMPTY_ITEM_ERROR

class HomePageTest(TestCase):

    def test_uses_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        # import pdb; pdb.set_trace()
        self.assertIsInstance(response.context['form'], ItemForm)
        
class ItemAndListModelsTest(TestCase):

  def test_cannot_save_empty_list_items(self):
    list_ = List.objects.create()
    item = Item(list=list_, text = '')
    with self.assertRaises(ValidationError):
      item.save()
      item.full_clean()

    
    def test_saves_and_retrieves_data_from_db(self):

        lst = List.objects.create()
        Item.objects.create(text='Item one', list=lst)
        Item.objects.create(text='Item two', list=lst)

        saved_items = Item.objects.all()

        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(saved_items[0].text, 'Item one')
        self.assertEqual(saved_items[1].text, 'Item two')

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        lst = List.objects.create()
        response = self.client.get(f'/list/{lst.id}/')
        
        self.assertTemplateUsed(response, 'list.html')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/list/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)

    def test_displays_only_items_from_that_list(self):
       
       correct_list = List.objects.create()
       other_list = List.objects.create()
       Item.objects.create(text='Item one', list=correct_list)
       Item.objects.create(text='Item two', list=correct_list)    

       response = self.client.get(f'/list/{correct_list.id}/')

       self.assertContains(response, 'Item one')
       self.assertContains(response, 'Item two')

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/list/{correct_list.id}/',
            data = {'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
                f'/list/{correct_list.id}/',
                data = {'item_text': 'A new item for an existing list'}
        )

        self.assertRedirects(response, f'/list/{correct_list.id}/')

    def test_validation_errors_end_up_on_lists_page(self):
        lst = List.objects.create()
        response = self.client.post(f'/list/{lst.id}/', data = {'item_text': ''})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = escape(EMPTY_ITEM_ERROR)
        self.assertContains(response, expected_error)
        
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

    def test_validation_errors_are_shown_on_home_page(self):
        response = self.client.post('/list/new/', data={'text': ''})
        import pdb; pdb.set_trace()
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))

    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/list/new/', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/list/new/', data={'text': ''})
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_invalid_list_items_are_not_saved_lists_and_items(self):
        self.client.post('/list/new/', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        # self.fail(form.as_p())
    
    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        # import pdb; pdb.set_trace()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR],
        )

