from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import leave_log, overtime_log, task_log, timesheet_log, user_details

# Create your views here.
from django.db.models.functions import Cast,Coalesce
from django.db.models import F,Sum
# from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField

from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response


from datetime import datetime
import time 
import random
import string
#EKO-L8HUG

@api_view(['POST'])
def login(request,format=None):
    try:
        username = (request.data)['username']
        password = (request.data)['password']
        print('username',username)
        try:
            a = user_details.objects.get(EMAIL = username)
        except:
            return Response({'status':'false',
                            'message':'user does not exist'})
        if check_password(password,a.PASSWORD):
            return Response({'status':'true',
                            'message':"login successful",
                            'emp_id':a.EMP_ID,
                            'token':a.TOKEN,
                            'user_type':a.USER_TYPE})
        else:
            return Response({'status':'false',
                            'message':"invalid credentials"})
    except:
        return Response({'status':'false',
                            'message':"invalid credentials"})

@api_view(['POST'])
def userDetails(request,format=None):
    emp_id = (request.data)['emp_id']
    # token = (request.headers)['Authorization']
    # check_token = user_details.objects.get(EMP_ID = emp_id)
    # if(check_token.TOKEN != token):
    #     return Response({'Message':'FALSE'})
    obj = user_details.objects.filter(EMP_ID = emp_id)\
                              .values('id')\
                              .annotate(name = F('NAME'),
                                        role = F('DESIGNATION')
                                       )\
                              .last()
    return Response({
                    'status':'true',
                    'message':"Successful",
                    'emp_details':obj,
                    })

@api_view(['POST'])
def leaves(request,format=None):
    emp_id = (request.data)['emp_id']
    # token = (request.headers)['Authorization']
    # check_token = user_details.objects.get(EMP_ID = emp_id)
    # if(check_token.TOKEN != token):
    #     return Response({'Message':'FALSE'})

    obj = leave_log.objects.filter(EMP_ID = emp_id)
    total_days = obj.aggregate(count = Coalesce(Sum('DURATION'), 0))['count']
    sick_leaves = obj.filter(TYPE='S').aggregate(count = Coalesce(Sum('DURATION'), 0))['count']
    casual_leaves = obj.filter(TYPE='C').aggregate(count = Coalesce(Sum('DURATION'), 0))['count']

    leave_data = obj.annotate(
                              leave_duration = F('DURATION_TYPE'),
                              start_date = F('START_DATE_TIMESTAMP'),
                              end_date = F('END_DATE_TIMESTAMP'),
                              leave_status = F('STATUS'),
                              leave_reason = F('REASON')
                             )\
                    .values('leave_duration','start_date','end_date','leave_status','leave_reason')\
                    .order_by('-start_date')
    leave_data = [{
                'heading':"Leaves",
                'total_value' : str(total_days),
                'unit' : 'days',
                'sub_data' : [
                              {
                                'sub_heading':'Sick',
                                'sub_value' : str(sick_leaves),
                                'sub_out_of' : '6',
                                'sub_unit' : 'days'
                              },
                              {
                                'sub_heading':'Casual',
                                'sub_value' : str(casual_leaves),
                                'sub_out_of' : '6',
                                'sub_unit' : 'days'
                              },
                              {
                                'sub_heading':'Paid',
                                'sub_value' : '0',
                                'sub_out_of' : '6',
                                'sub_unit' : 'days'
                              }
                             ]
                 }]
    

    leave_stats = {
                 'leave_history':leave_data,
                 'leave_data': leave_data
                  }
    return Response({
                    'status':'true',
                    'message':"Successful",
                    'leave_stats':leave_stats
                    })

@api_view(['POST'])
def onDesk(request,format=None):
    emp_id = (request.data)['emp_id']
    # token = (request.headers)['Authorization']
    # check_token = user_details.objects.get(EMP_ID = emp_id)
    # if(check_token.TOKEN != token):
    #     return Response({'Message':'FALSE'})
    obj = timesheet_log.objects.filter(EMP_ID = emp_id).exclude(SHOW_VALIDATION = 0)
    total_days = obj.count()
    home = obj.filter(WORK_TYPE = 'H').count()
    office = obj.filter(WORK_TYPE = 'O').count()
    on_desk = {
                'heading':"On Desk",
                'total_value' : str(total_days),
                'unit' : 'days',
                'sub_data' : [
                              {
                                'sub_heading':'WFO',
                                'sub_value' : str(office),
                                'sub_unit' : 'days'
                              },
                              {
                                'sub_heading':'WFH',
                                'sub_value' : str(home),
                                'sub_unit' : 'days'
                              }]
               }   
    return Response({
                    'status':'true',
                    'message':"Successful",
                    'on_desk':on_desk
                    }) 

@api_view(['POST'])
def overtime(request,format=None):
    emp_id = (request.data)['emp_id']
    # token = (request.headers)['Authorization']
    # check_token = user_details.objects.get(EMP_ID = emp_id)
    # if(check_token.TOKEN != token):
    #     return Response({'Message':'FALSE'})
    obj = overtime_log.objects.filter(EMP_ID = emp_id)
    total_overtime = obj.aggregate(count = Coalesce(Sum('DURATION'), 0))['count']
    home = obj.filter(WORK_TYPE = 'H').aggregate(count = Coalesce(Sum('DURATION'), 0))['count']
    office = obj.filter(WORK_TYPE = 'O').aggregate(count = Coalesce(Sum('DURATION'), 0))['count']
    overtime = {
                'heading':"Overtime",
                'total_value' : str(total_overtime),
                'unit' : 'hrs',
                'sub_data' : [
                              {
                                'sub_heading':'WFO',
                                'sub_value' : str(office),
                                'sub_unit' : 'hrs'
                              },
                              {
                                'sub_heading':'WFH',
                                'sub_value' : str(home),
                                'sub_unit' : 'hrs'
                              }]
               }   
    return Response({
                    'status':'true',
                    'message':"Successful",
                    'overtime' :overtime
                    })


@api_view(['POST'])
def clockInOut(request,format=None):
  emp_id = (request.data)['emp_id']
  r_type = (request.data)['r_type']
  #--------- for get request ----------------------------
  if r_type == 'G':
    emp_id = (request.data)['emp_id']
    cur_date =  datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y"))
    try:
      timesheet_log.objects.get(EMP_ID = emp_id,DATE = cur_date)
    except:
      data = timesheet_log(EMP_ID = emp_id,
                    DATE = cur_date
                    )
      data.save()
    obj = timesheet_log.objects.filter(EMP_ID = emp_id,DATE = cur_date).values().last()
    try:
      clock_in = datetime.fromtimestamp(obj['CLOCK_IN_TIMESTAMP']).strftime('%I:%M %p')
    except:
      clock_in = 0
    
    try:
      clock_out = datetime.fromtimestamp(obj['CLOCK_OUT_TIMESTAMP']).strftime('%I:%M %p')
    except:
      clock_out = 0

    return Response({'status':'true',
                       'message':"Successful",
                       'clock_in': clock_in,
                       'clock_out': clock_out,
                    })

  #--------- for post request ----------------------------
  elif r_type == 'P':
    t_type = (request.data)['t_type']
  
    cur_date = datetime.timestamp(datetime.strptime(datetime.now().strftime('%d-%m-%Y'),"%d-%m-%Y"))
    now = int(datetime.timestamp(datetime.now()))
    obj =  timesheet_log.objects.filter(EMP_ID = emp_id,DATE = cur_date)
     
      #---------------- for clock in ----------------------------
    if t_type == 'CI':
      obj.update(
              CLOCK_IN = datetime.fromtimestamp(now).strftime('%d-%m-%Y %H:%M:%S'),
              CLOCK_IN_TIMESTAMP  = now,
              SHOW_VALIDATION = 1 
                )
      
      obj = timesheet_log.objects.filter(EMP_ID = emp_id,DATE = cur_date).values().last()
      try:
        clock_in = datetime.fromtimestamp(obj['CLOCK_IN_TIMESTAMP']).strftime('%I:%M %p')
      except:
        clock_in = 0
      
      try:
        clock_out = datetime.fromtimestamp(obj['CLOCK_OUT_TIMESTAMP']).strftime('%I:%M %p')
      except:
        clock_out = 0
      return Response({'status':'true',
                       'message':"Successful",
                       'clock_in': clock_in,
                       'clock_out': clock_out,
                    })

      #----------------- for clock out ----------------------------------------------
    elif t_type == 'CO':
      duration = now - obj['CLOCK_IN_TIMESTAMP']
      obj.update(
              CLOCK_OUT = datetime.fromtimestamp(now).strftime('%d-%m-%Y %H:%M:%S'),
              CLOCK_OUT_TIMESTAMP  = now,
              DURATION = duration
                )
      obj = timesheet_log.objects.filter(EMP_ID = emp_id,DATE = cur_date).values().last()
      try:
        clock_in = datetime.fromtimestamp(obj['CLOCK_IN_TIMESTAMP']).strftime('%I:%M %p')
      except:
        clock_in = 0
      
      try:
        clock_out = datetime.fromtimestamp(obj['CLOCK_OUT_TIMESTAMP']).strftime('%I:%M %p')
      except:
        clock_out = 0
      return Response({'status':'true',
                       'message':"Successful",
                       'clock_in': clock_in,
                       'clock_out': clock_out,
                    })


@api_view(['POST'])
def taskLog(request,format=None):
  emp_id = (request.data)['emp_id']
  obj = task_log.objects.filter(EMP_ID = emp_id).order_by('-DATE_TIMESTAMP')
  res = obj.values('DATE').annotate(
                                    date = F('DATE'),
                                    projects = F('PROJECT'),
                                    tasks = F('TASK'),
                                    color = F('PROJECT_COLOR'),
                                    remark = F('REMARKS')
                                   )

  return Response({'status':'true',
                       'message':"Successful",
                       'task_log': res
                    })



# def index(request):
#     password = '1234'

#     a = user_details.objects.all().values().last()
#     emp_id = a['EMP_ID']
#     psw = make_password(password, emp_id, 'argon2') #python -m pip install django[argon2]
#     user_details.objects.filter(EMP_ID = emp_id).update(PASSWORD = psw)
    
#     return HttpResponse('Hello')


# def index(request):
#     psw = '1234'

#     a =user_details.objects.filter(EMP_ID = 'EKO-L8HUG').values().last()
#     token = make_password(a['EMAIL']+psw)
#     user_details.objects.filter(EMP_ID = 'EKO-L8HUG').update(TOKEN=token)
#     return HttpResponse('hello')


def create_user(request):
  # EMP_ID = 'EKO-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
  # NAME = 'Amrit Singh'
  # DESIGNATION = 'Backend Developer'
  # EMAIL = 'amrit.s@ekoinfomatics.com'
  # JOINING_DATE = '3-9-2022'
  # JOINING_DATE_TIMESTAMP = datetime.timestamp(datetime.strptime(JOINING_DATE,"%d-%m-%Y"))
  # USER_TYPE = 'U'
  # psw = '1234'
  # PASSWORD = make_password(psw, EMP_ID, 'argon2')
  # TOKEN = make_password(EMAIL+psw)

  # data = user_details(
  #                     EMP_ID = EMP_ID,
  #                     NAME = NAME,
  #                     DESIGNATION = DESIGNATION,
  #                     EMAIL = EMAIL,
  #                     JOINING_DATE = JOINING_DATE,
  #                     JOINING_DATE_TIMESTAMP = JOINING_DATE_TIMESTAMP,
  #                     USER_TYPE = USER_TYPE,
  #                     PASSWORD = PASSWORD,
  #                     TOKEN = TOKEN
  #                    )
  # data.save()
  timesheet_log.objects.all().update(SHOW_VALIDATION=0)
  return HttpResponse('hello')



  