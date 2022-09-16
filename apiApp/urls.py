from django.urls import path
import apiApp.views as views
 
urlpatterns = [
    # path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('leaves',views.leaves,name='leaves'),
    
]