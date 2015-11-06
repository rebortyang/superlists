__author__ = 'yangjiebin'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.broswer = webdriver.Firefox()
        self.broswer.implicitly_wait(3)

    def tearDown(self):
        self.broswer.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #there is a web site name 'TO-DO'
        #so i open it
        self.broswer.get('http://localhost:8000')
        # the title and head has a word : 'To-Do'
        time.sleep(8)
        self.assertIn('To-Do lists', self.broswer.title)
        header_text = self.broswer.find_element_by_tag_name('h1').text
        self.assertEqual('To-Do lists', header_text)


        #it call you to write one 'to-do' thing
        inputbox = self.broswer.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #i input 'go to HK'
        inputbox.send_keys('go to HK')

        #enter,web refresh
        inputbox.send_keys(Keys.ENTER)

        #web table show "1. go to HK"
        table = self.broswer.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: go to HK', [row.text for row in rows])

        #web still has a input text.
        #i input again, 'buy phone'
        inputbox = self.broswer.find_element_by_id('id_new_item')
        inputbox.send_keys('buy phone')
        inputbox.send_keys(Keys.ENTER)


        #web page refresh again. there are two 'to-do'
        #the web create a URL for me.and page show me some thing about it.
        table = self.broswer.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2: buy phone', [row.text for row in rows])

        #visit the URL.find 'to-do' still in.
        #sleep.
        self.fail('finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')