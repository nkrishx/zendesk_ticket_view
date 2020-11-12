from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get(reverse(""))
        self.assertEqual(response.status_code, 200)
