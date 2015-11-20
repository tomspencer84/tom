# https://docs.djangoproject.com/en/1.7/intro/tutorial01/

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
        question_text = models.CharField(max_length=200, default='default')
        pub_date = models.DateTimeField('date published',default=timezone.now) #default=timezone.now()
        def __unicode__(self):
                return self.question_text

class Choice(models.Model):
        question = models.ForeignKey(Question,default=1)
        choice_text = models.CharField(max_length=200, default='default')
        votes = models.IntegerField(default=0)
        def __unicode__(self):
                return self.choice_text
        def was_published_recently(self):
                return self.pub_date >= timezone.now() - datetime.timedelta(days=1)