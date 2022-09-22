from django.urls import path
import apiApp.views as views
 
urlpatterns = [
    # path('',views.create_user,name='create_user'),
    path('login',views.login,name='login'),
    path('leaves',views.leaves,name='leaves'),
    path('onDesk',views.onDesk,name='onDesk'), 
    path('overtime',views.overtime,name='overtime'),
    path('userDetails',views.userDetails,name='userDetails'),
    path('clockInOut',views.clockInOut,name='clockInOut'),
    path('taskLog',views.taskLog,name='taskLog'),
    
    
]