__author__ = 'yangjiebin'

from selenium import webdriver
import unittest

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
        self.broswer.implicitly_wait(8)
        self.assertIn('To-Do lists', self.broswer.title)
        self.fail('finish the test!')

        #it call you to write one 'to-do' thing

        #i input 'go to HK'
        #enter,web refresh
        #web table show "1. go to HK"
        #web still has a input text.
        #i input again, 'buy phone'
        #web page refresh again. there are two 'to-do'
        #the web create a URL for me.and page show me some thing about it.

        #visit the URL.find 'to-do' still in.
        #sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')