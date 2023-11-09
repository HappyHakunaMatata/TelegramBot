"""
Definition of models.
"""

from email import message
from pyexpat import model
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class DailyMessages(models.Model):
    primaryKey = models.AutoField(primary_key=True)
    text = models.TextField()
    timestamp = models.DateTimeField()
    CreateDateTime = models.DateTimeField(auto_now_add=True)
    
class DateTimeMessages(models.Model):
    primaryKey = models.AutoField(primary_key=True)
    textfield = models.TextField()
    timestampfield = models.DateTimeField()
    datefield = models.DateTimeField()
    CreateDateTime = models.DateTimeField(auto_now_add=True)

class WeeklyMessages(models.Model):
    primaryKey = models.AutoField(primary_key=True)
    AddWeeklyMessage = models.TextField()
    AddTimestamp = models.DateTimeField()
    AddWeek = models.TextField()
    CreateDateTime = models.DateTimeField(auto_now_add=True)
    
class ProgressBarStatus(models.Model):
    ProgressbarPKey = models.AutoField(primary_key=True)
    ProgressbarStatus = models.BooleanField(default=False)