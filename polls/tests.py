import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Questions


class QuestionsMethodTests(TestCase):
    def was_published_recently_with_future_questions_tests(self):
        """ was_published_recently() should return False for questions whose published date is in the future """
        time = timezone.now()+datetime.timedelta(days=30)
        future_questions = Questions(pub_date=time)
        self.assertEqual(future_questions.was_published_recently(), False)
