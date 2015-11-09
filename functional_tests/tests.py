__author__ = 'yangjiebin'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest, time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.broswer = webdriver.Firefox()
        self.broswer.implicitly_wait(3)

    def tearDown(self):
        self.broswer.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.broswer.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #there is a web site name 'TO-DO'
        #so i open it
        self.broswer.get(self.live_server_url)
        # the title and head has a word : 'To-Do'

        self.assertIn('To-Do lists', self.broswer.title)
        header_text = self.broswer.find_element_by_tag_name('h1').text
        self.assertEqual('To-Do lists', header_text)


        #it call you to write one 'to-do' thing
        inputbox = self.broswer.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #i input 'go to HK'
        inputbox.send_keys('go to HK')

        #enter,web bring to a new URL
        #the page show list like '1: go to HK'
        inputbox.send_keys(Keys.ENTER)

        time.sleep(5)

        edith_list_url = self.broswer.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: go to HK')

        #web still has a input text.
        #i input again, 'buy phone'
        inputbox = self.broswer.find_element_by_id('id_new_item')
        inputbox.send_keys('buy phone')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(5)
        #web page refresh again. there are two 'to-do'
        #the web create a URL for me.and page show me some thing about it.
        self.check_for_row_in_list_table('1: go to HK')
        self.check_for_row_in_list_table('2: buy phone')

        #now, there is a boy tom visit the web_page

        ##we use the new browser
        ## protect my info safe.
        self.broswer.quit()
        self.broswer = webdriver.Firefox()

        time.sleep(5)

        #tom visit index
        #he can not see my list
        self.broswer.get(self.live_server_url)
        page_text = self.broswer.find_element_by_tag_name('body').text
        self.assertNotIn('go to HK', page_text)
        self.assertNotIn('buy phone', page_text)

        #tom input a item, make a new list
        inputbox = self.broswer.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)

        #tom get his own URL
        tom_list_url = self.broswer.current_url
        self.assertRegexpMatches(tom_list_url, '/lists/.+')
        self.assertNotEqual(edith_list_url, tom_list_url)

        #this page not has my list content
        page_text = self.broswer.find_element_by_tag_name('body').text
        self.assertNotIn('go to HK', page_text)
        self.assertIn('buy milk', page_text)

        #visit the URL.find 'to-do' still in.
        #sleep.
        self.fail('finish the test!')

