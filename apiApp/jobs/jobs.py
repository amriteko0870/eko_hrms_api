from django.conf import settings
from apiApp.models import task_log, timesheet_log,user_details
from datetime import datetime

def schedule_api():
    user_list = user_details.objects.values_list('EMP_ID',flat=True)
    for i in list(user_list):
        obj = timesheet_log(
                            EMP_ID = i,
                            DATE = datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y")),
                            SHOW_VALIDATION = 0,
                            DAY_TYPE = "W"
                           )
        obj.save()

        task = task_log(
                        EMP_ID = i,
                        DATE = datetime.now().strftime('%d %b %Y'),
                        DATE_TIMESTAMP = datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y")),
                        TASK = 'add your tasks',
                        PROJECT = '',
                        PROJECT_COLOR = '',
                        REMARKS = 'not added',
                       )
        task.save()

def on_leave():
    user_list = user_details.objects.values_list('EMP_ID',flat=True)
    for i in list(user_list):
        obj = timesheet_log(
                            EMP_ID = i,
                            DATE = datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y")),
                            SHOW_VALIDATION = 1,
                            DAY_TYPE = 'H'
                           )
        obj.save()
        task = task_log(
                        EMP_ID = i,
                        DATE = datetime.now().strftime('%d %b %Y'),
                        DATE_TIMESTAMP = datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y")),
                        TASK = 'No Task',
                        PROJECT = '',
                        PROJECT_COLOR = '',
                        REMARKS = 'Holiday',
                       )
        task.save()
