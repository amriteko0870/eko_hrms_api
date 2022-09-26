from itertools import groupby
from operator import itemgetter
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import leave_log, overtime_log, projects_log, task_log, timesheet_log, user_details

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
import pandas as pd




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


@api_view(['POST'])
def taskLogUpdation(request,format=None):
  emp_id = (request.data)['emp_id']
  date = (request.data)['date']
  r_type = (request.data)['r_type']
  print('################### ',emp_id,date,r_type)
  timestamp = time.mktime(datetime.strptime(date, "%d-%m-%Y").timetuple())
  if r_type == 'G':
    emp_id = (request.data)['emp_id']
  date = (request.data)['date']
  r_type = (request.data)['r_type']
  print('################### ',emp_id,date,r_type)
  timestamp = time.mktime(datetime.strptime(date, "%d-%m-%Y").timetuple())
  if r_type == 'G':
    obj = task_log.objects.filter(
                                  EMP_ID = emp_id,
                                  DATE_TIMESTAMP = timestamp
                                 )
    cur_proj_list = (obj.values_list('PROJECT',flat=True))
    if list(cur_proj_list)[-1] == '':
      all_proj_list = projects_log.objects.filter(EMP_ID = emp_id).values_list('PROJECT','PROJECT_COLOR')
      c=1
      data = [] 
      for i in all_proj_list:
        data.append({
        'id':c,
        'task' : 'add your task',
        'project' : i[0],
        'project_color' : i[1],
        }) 
        c = c +1
    else:
      data =  obj.values('id').annotate(
                                      date = F('DATE'),
                                      task = F('TASK'),
                                      project = F('PROJECT'),
                                      project_color = F('PROJECT_COLOR'),
                                      timestamp = F('DATE_TIMESTAMP')
                                      )
      e_proj_list = list(data.values_list('project',flat=True))
      all_proj_list = list(projects_log.objects.filter(EMP_ID = emp_id).values_list('PROJECT',flat=True))
      data = list(data)
      prev_state = data[-1]
      c = prev_state['id']
      n_project = list(projects_log.objects.filter(EMP_ID = emp_id,STATUS = 'I')\
                                           .exclude(PROJECT__in = e_proj_list)\
                                           .values_list('PROJECT','PROJECT_COLOR'))
      for i in n_project:
        c = c+1
        data.append({
              "id": c,
              "date": prev_state['date'],
              "task": "add your tasks",
              "project": i[0],
              "project_color": i[1],
              "timestamp": prev_state['timestamp']
              })
    res = {
          'date':date,
          'remark': obj.values('REMARKS').last()['REMARKS'],
          'task_array':data,
    }
    return Response(res)
  elif r_type == 'P':
    data = (request.data)['task_array']
    remark = (request.data)['remark']
    data = pd.DataFrame(data).to_dict(orient='list')
    obj = task_log.objects.filter(
                            EMP_ID = emp_id,
                            DATE_TIMESTAMP = d
                            )
    obj.update(
               TASK = "|".join(data['task']),
               PROJECT = "|".join(data['project']),
               PROJECT_COLOR = "|".join(data['project_color']),
               REMARKS = remark,
              ) 
    res = task_log.objects.filter(EMP_ID = emp_id).order_by('-DATE_TIMESTAMP')
    res = obj.values('DATE').annotate(
                                      date = F('DATE'),
                                      projects = F('PROJECT'),
                                      tasks = F('TASK'),
                                      color = F('PROJECT_COLOR'),
                                      remark = F('REMARKS')
                                    )
    return Response({'status':'true',
                     'message':"Successful",
                    #  'task_array': data,
                     'updated_array': res,
                    })
  