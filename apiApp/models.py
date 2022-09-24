from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class user_details(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)
    NAME = models.CharField(max_length=300,null = True)
    DESIGNATION = models.CharField(max_length=300,null = True)
    EMAIL = models.CharField(max_length=300,null = True)
    PASSWORD = models.CharField(max_length=300,null = True)

    JOINING_DATE = models.CharField(max_length=300,null = True)
    JOINING_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    USER_TYPE = models.CharField(max_length=1,null = True) # (S,U) S -> Super-user , U -> User
    TOKEN = models.CharField(max_length=300,null = True) # username + passowrd

class timesheet_log(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)

    CLOCK_IN = models.CharField(max_length=300,null = True)
    CLOCK_IN_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    CLOCK_OUT = models.CharField(max_length=300,null = True)
    CLOCK_OUT_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    DATE = models.BigIntegerField(null=True,blank=True)
    WORK_TYPE = models.CharField(max_length=1,null = True) # (O,H) O -> Office , H -> HOME
    SHOW_VALIDATION = models.IntegerField(null=True,blank=True)
    DAY_TYPE = models.CharField(max_length=1,null = True) # (W,L,H) W -> Working , L -> Leave , H -> Holiday
    DURATION = models.BigIntegerField(null=True,blank=True)

class overtime_log(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)
    WORK_TYPE = models.CharField(max_length=1,null = True) # (O,H) O -> Office , H -> HOME
    DURATION = models.BigIntegerField(null=True,blank=True) # in minutes
    DATE = models.CharField(max_length=300,null = True)
    DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

class leave_log(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)
    DURATION_TYPE = models.CharField(max_length=1,null = True) # (H,F) H -> Half-day , F -> Full-day
    
    START_DATE = models.CharField(max_length=300,null = True)
    START_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)
    
    END_DATE = models.CharField(max_length=300,null = True)
    END_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    TYPE = models.CharField(max_length=1,null = True) # (C,S) C -> Casual , S -> Sick
    REASON = models.TextField()
    STATUS = models.CharField(max_length=1,null = True) #(A,P,D) A-> Approved P-> Pending D -> Declined
    DURATION = models.IntegerField(null=True,blank=True)

class task_log(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)

    DATE = models.CharField(max_length=300,null = True)
    DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    TASK = models.TextField()
    PROJECT = models.CharField(max_length=300,null = True)
    PROJECT_COLOR = models.CharField(max_length=300,null = True)
    REMARKS = models.CharField(max_length=300,null = True)

class event_log(models.Model):
    START_DATE = models.CharField(max_length=300,null = True)
    START_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    END_DATE = models.CharField(max_length=300,null = True)
    END_DATA_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    EVENT_NAME = models.CharField(max_length=300,null = True)


class projects_log(models.Model):
    EMP_ID = models.CharField(max_length=300,null = True)
    PROJECT = models.CharField(max_length=300,null = True)
    STATUS = models.CharField(max_length=1,null = True) # (I,O,C) I -> In progress , O -> On hold , C -> Complete
    PROJECT_COLOR = models.CharField(max_length=300,null = True)