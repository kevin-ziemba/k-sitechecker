import website_checker
import unittest

class TestWebsiteChecker(unittest.TestCase):

    def test_https(self):
        self.assertEqual(website_checker.url_status_code('https://www.google.ca/'), "200")

    def test_http(self):
        self.assertEqual(website_checker.url_status_code('http://espn.com'), "200")

    def test_fake_address(self):
        self.assertNotEqual(website_checker.url_status_code('ht://espn.com'), "200")
        self.assertNotEqual(website_checker.url_status_code('http://espn'), "200")
        self.assertNotEqual(website_checker.url_status_code('http://thisdoesnotexist1klhbndswjlflhfk3423.com'), "200")

if __name__ == '__main__':
    unittest.main()