from pyexpat import model
from django.db import models

# Create your models here.


class user_details(models.Model):
    EMP_ID = models.CharField(max_length=300)
    NAME = models.CharField(max_length=300)
    DESIGNATION = models.CharField(max_length=300)
    EMAIL = models.CharField(max_length=300)
    PASSWORD = models.CharField(max_length=300)

    JOINING_DATE = models.CharField(max_length=300)
    JOINING_DATE_TIMESTAMP = models.BigIntegerField()

    USER_TYPE = models.CharField(max_length=1) # (S,U) S -> Super-user , U -> User
    TOKEN = models.CharField(max_length=300) # username + passowrd

class timesheet_log(models.Model):
    EMP_ID = models.CharField(max_length=300)

    CLOCK_IN = models.BigIntegerField()
    CLOCK_IN_TIMESTAMP = models.BigIntegerField()

    CLOCK_OUT = models.BigIntegerField()
    CLOCK_OUT_TIMESTAMP = models.BigIntegerField()

    WORK_TYPE = models.CharField(max_length=1) # (O,H) O -> Office , H -> HOME
    SHOW_VALIDATION = models.IntegerField()

class overtime_log(models.Model):
    EMPT_ID = models.CharField(max_length=300)
    WORK_TYPE = models.CharField(max_length=1) # (O,H) O -> Office , H -> HOME
    DURATION = models.BigIntegerField() # in minutes

class leave_log(models.Model):
    EMP_ID = models.CharField(max_length=300)
    DURATION_TYPE = models.CharField(max_length=1) # (H,F) H -> Half-day , F -> Full-day
    
    START_DATE = models.CharField(max_length=300)
    START_DATE_TIMESTAMP = models.BigIntegerField()
    
    END_DATE = models.CharField(max_length=300)
    END_DATE_TIMESTAMP = models.BigIntegerField()

    TYPE = models.CharField(max_length=1) # (C,S) C -> Casual , S -> Sick
    REASON = models.TextField()
    STATUS = models.CharField(max_length=1) #(A,P,D) A-> Approved P-> Pending D -> Declined

class task_log(models.Model):
    EMP_ID = models.CharField(max_length=300)

    DATE = models.CharField(max_length=300)
    DATE_TIMESTAMP = models.BigIntegerField()

    TASK = models.TextField()
    PROJECT = models.CharField(max_length=300)
    PROJECT_COLOR = models.CharField(max_length=300)
    REMARKS = models.CharField(max_length=300)

class event_log(models.Model):
    START_DATE = models.CharField(max_length=300)
    START_DATE_TIMESTAMP = models.BigIntegerField()

    END_DATE = models.CharField(max_length=300)
    END_DATA_TIMESTAMP = models.BigIntegerField()

    EVENT_NAME = models.CharField(max_length=300)

