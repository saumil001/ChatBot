from __future__ import unicode_literals
from djongo import models
from django.utils import timezone


# Create your models here.

class ChattingBot(models.Model):
    name = models.CharField('Your Name', max_length=120, blank=False, default='om')
    event_date = models.DateTimeField('Date Of Birth', default=timezone.now)


