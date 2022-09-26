from django.urls import path
import apiApp.views as views
import apiApp.self_views.task as task
 
urlpatterns = [
    # path('',views.create_user,name='create_user'),
    # path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('leaves',views.leaves,name='leaves'),
    path('onDesk',views.onDesk,name='onDesk'), 
    path('overtime',views.overtime,name='overtime'),
    path('userDetails',views.userDetails,name='userDetails'),
    path('clockInOut',views.clockInOut,name='clockInOut'),


    path('taskLog',task.taskLog,name='taskLog'),
    path('taskLogUpdation',task.taskLogUpdation,name = 'taskLogUpdation'),


    path('projectAdd',views.projectAdd,name='projectAdd'),
    path('projectGet',views.projectGet,name='projectGet'),
    
]