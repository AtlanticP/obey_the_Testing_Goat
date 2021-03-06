from django.test import LiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
from selenium.common.exceptions import WebDriverException
import time
MAX_WAIT = 3

class FucntionalTest(LiveServerTestCase):


    def setUp(self):  
        
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Firefox(firefox_options=options) 
        staging_server = os.environ.get('STAGING_SERVER')
        
        if staging_server:
            self.live_server_url = 'http://' + staging_server
            print(self.live_server_url)
    
    def tearDown(self):  
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        
        start_time = time.time()
        
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])

                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        
        start_time = time.time()
        
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])

                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')