from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login
from schedule.models import Schedule


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.normal_user = User.objects.create_user(username='test2', password='t2', email='t2@t.pl')
        self.super_user = User.objects.create_superuser(username='test', password='t', email='t@t.pl')

    def test_index_view(self):
        self.client.login(username='test2', password='t2', email='t2@t.pl')
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/index.html')

    def test_schedule_add_view_forbidden(self):
        self.client.login(username='test2', password='t2', email='t2@t.pl')
        response = self.client.get(reverse('schedule-add'))
        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_schedule_add_view_superuser(self):
        self.client.login(username='test', password='t', email='t@t.pl')
        response = self.client.get(reverse('schedule-add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/schedule-add.html')
