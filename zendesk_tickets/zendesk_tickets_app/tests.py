from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from nose.tools import assert_is_not_none
import requests
from . import views
from .services import get_tickets,get_ticket_details

# Create your tests here.

class HomePageTests(SimpleTestCase):
    #test for Homepage
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('HomeView'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('HomeView'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<li>Connect to the Zendesk API.</li>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_ticket_list_request_response(self):
        response = get_tickets()
        assert_is_not_none(response)

class TicketViewerTests(SimpleTestCase):
    #test for ticket viewer page
    def test_ticketviewer_page_status_code(self):
        response = self.client.get('/connect',follow=True)
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('ConnectView'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('ConnectView'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'connect.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/connect',follow=True)
        self.assertContains(response, '<h1 class="display-8">Ticket Viewer</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/connect',follow=True)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
