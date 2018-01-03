from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MyTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()

	def test_my_test(self):

		# self.browser.get(self.live_server_url)
		# print(self.browser.get(self.live_server_url))

		self.browser.get(self.live_server_url)

		self.assertIn('Home page', self.browser.title)