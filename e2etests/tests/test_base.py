from unittest import TestCase

from selene import config
from selene.browsers import BrowserName


class BaseTest(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        config.base_url = 'http://127.0.0.1:8000'
