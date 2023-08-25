import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from schedule.models import Schedule, Shift, Slot, Person


class ModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.schedule = Schedule.objects.create(
            name='schedule test',
            start_day = datetime.datetime(2023, 8, 1),
            end_date = datetime.datetime(2023, 8, 31)
        )

    def test_correct_schedule_model(self):
        self.assertEqual(self.schedule.name, 'schedule test')