from django.urls import path
import apiApp.views as views
 
urlpatterns = [
    # path('',views.create_user,name='create_user'),
    # path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('leaves',views.leaves,name='leaves'),
    path('onDesk',views.onDesk,name='onDesk'), 
    path('overtime',views.overtime,name='overtime'),
    path('userDetails',views.userDetails,name='userDetails'),
    path('clockInOut',views.clockInOut,name='clockInOut'),
    path('taskLog',views.taskLog,name='taskLog'),
    path('taskLogUpdation',views.taskLogUpdation,name='taskLogUpdation'),
    

    path('projectAdd',views.projectAdd,name='projectAdd'),
    path('projectGet',views.projectGet,name='projectGet'),
    
]