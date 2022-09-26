from apiApp.models import task_log, timesheet_log,user_details
from datetime import datetime
import calendar


def on_working():
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



def working_days():
    cur_date = datetime.now()
    # timestamp = time.mktime(datetime.strptime(string_date, '%d-%m-%Y').timetuple())
    if cur_date.weekday() == 6:
        on_leave()
    elif cur_date.weekday() == 5:
        cal = calendar.monthcalendar(cur_date.year, cur_date.month)
        try:
            sat_list = [cal[0][calendar.SATURDAY],
                        cal[1][calendar.SATURDAY],
                        cal[2][calendar.SATURDAY],
                        cal[3][calendar.SATURDAY],
                        cal[4][calendar.SATURDAY]]
        except:
            sat_list = [cal[0][calendar.SATURDAY],
                        cal[1][calendar.SATURDAY],
                        cal[2][calendar.SATURDAY],
                        cal[3][calendar.SATURDAY]]
        if 0 in sat_list:
            sat_list.remove(0)
        if cur_date.day in sat_list[0::2]:
            on_leave()
        else:
            on_working()
    else:
        on_working()


