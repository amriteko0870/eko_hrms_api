from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import user_details

# Create your views here.
from django.db.models.functions import Cast
from django.db.models import F,TimeField


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
