from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page#(2)

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')  # 1
        self.assertTemplateUsed(response, 'home.html')  # 3

