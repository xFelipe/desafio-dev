from django.test import TestCase
from django.test import Client
from django.urls import resolve

# Create your tests here.

class TestMainPage(TestCase):
    def test_get_main_page_has_status_code_200(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)
