from django.test import SimpleTestCase
from django.urls import reverse, resolve
from schedule.views import IndexView


class TestUrls(SimpleTestCase):

    def test_index(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexView)