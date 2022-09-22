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
    JOINING_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    USER_TYPE = models.CharField(max_length=1) # (S,U) S -> Super-user , U -> User
    TOKEN = models.CharField(max_length=300) # username + passowrd

class timesheet_log(models.Model):
    EMP_ID = models.CharField(max_length=300)

    CLOCK_IN = models.CharField(max_length=300)
    CLOCK_IN_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    CLOCK_OUT = models.CharField(max_length=300)
    CLOCK_OUT_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    DATE = models.BigIntegerField(null=True,blank=True)
    WORK_TYPE = models.CharField(max_length=1) # (O,H) O -> Office , H -> HOME
    SHOW_VALIDATION = models.IntegerField(null=True,blank=True)
    DAY_TYPE = models.CharField(max_length=1) # (W,L,H) W -> Working , L -> Leave , H -> Holiday
    DURATION = models.BigIntegerField(null=True,blank=True)

class overtime_log(models.Model):
    EMP_ID = models.CharField(max_length=300)
    WORK_TYPE = models.CharField(max_length=1) # (O,H) O -> Office , H -> HOME
    DURATION = models.BigIntegerField(null=True,blank=True) # in minutes
    DATE = models.CharField(max_length=300)
    DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

class leave_log(models.Model):
    EMP_ID = models.CharField(max_length=300)
    DURATION_TYPE = models.CharField(max_length=1) # (H,F) H -> Half-day , F -> Full-day
    
    START_DATE = models.CharField(max_length=300)
    START_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)
    
    END_DATE = models.CharField(max_length=300)
    END_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    TYPE = models.CharField(max_length=1) # (C,S) C -> Casual , S -> Sick
    REASON = models.TextField()
    STATUS = models.CharField(max_length=1) #(A,P,D) A-> Approved P-> Pending D -> Declined
    DURATION = models.IntegerField(null=True,blank=True)

class task_log(models.Model):
    EMP_ID = models.CharField(max_length=300)

    DATE = models.CharField(max_length=300)
    DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    TASK = models.TextField()
    PROJECT = models.CharField(max_length=300)
    PROJECT_COLOR = models.CharField(max_length=300)
    REMARKS = models.CharField(max_length=300)

class event_log(models.Model):
    START_DATE = models.CharField(max_length=300)
    START_DATE_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    END_DATE = models.CharField(max_length=300)
    END_DATA_TIMESTAMP = models.BigIntegerField(null=True,blank=True)

    EVENT_NAME = models.CharField(max_length=300)

