from time import struct_time

from django.test import TestCase
from feedparser import parse


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        
    def test_home_get(self):
        """GET -> deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_home_template(self):
        """deve usar o index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')


class FeedTest(TestCase):
    def setUp(self):
        self.rss = parse('http://pythonclub.com.br/feeds/all.atom.xml')

    def test_feed_get(self):
        """Feed deve retornar com status code 200"""
        self.assertEqual(200, self.rss['status'])

    def test_feed_title(self):
        """Deve retornar True para um title não vazio"""
        self.assertTrue(self.rss['feed']['title'] is not '')

    def test_feed_last_updated_time(self):
        """Deve retornar um obj struct_time"""
        self.assertIsInstance(self.rss['updated_parsed'], struct_time)
