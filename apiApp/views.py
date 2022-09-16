from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import leave_log, user_details

# Create your views here.
from django.db.models.functions import Cast
from django.db.models import F,Sum
# from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField

from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response




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
def leaves(request,format=None):
    emp_id = (request.data)['emp_id']
    # token = (request.headers)['Authorization']
    # check_token = user_details.objects.get(EMP_ID = emp_id)
    # if(check_token.TOKEN != token):
    #     return Response({'Message':'FALSE'})

    obj = leave_log.objects.filter(EMP_ID = emp_id)
    total_days = obj.aggregate(count = Sum('DURATION'))['count']
    sick_leaves = obj.filter(TYPE='S').aggregate(count = Sum('DURATION'))['count']
    casual_leaves = obj.filter(TYPE='C').aggregate(count = Sum('DURATION'))['count']

    leave_data = obj.annotate(
                              leave_duration = F('DURATION_TYPE'),
                              start_date = F('START_DATE_TIMESTAMP'),
                              end_date = F('END_DATE_TIMESTAMP'),
                              leave_status = F('STATUS'),
                              leave_reason = F('REASON')
                             )\
                    .values('leave_duration','start_date','end_date','leave_status','leave_reason')\
                    .order_by('-start_date')

    leave_stats = {
                 'total_days':total_days,
                 'total_sick_days':sick_leaves,
                 'total_casual_days':casual_leaves,
                 'leave_history':leave_data
                  }
    return Response({
                    'status':'true',
                    'message':"Successful",
                    'leave_stats':leave_stats
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
