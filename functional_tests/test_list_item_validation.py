from .base import FucntionalTest


class ItemValidationTest(FucntionalTest):

    # @skip
    def test_cannot_add_empty_list_items(self):

        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)



        # The home page refreshes, and there is an error message saying 
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item",
        )

        # She tries again with some text for the item, which now works
        
        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can coorect it by filling some text in
        self.fail('write me')
        
