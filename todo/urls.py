from django.urls import path
from .import views

app_name='todo'
urlpatterns = [
    path('',views.index,name='index'),
    path('loginUser/',views.loginUser,name='loginUser'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('createNewUser/',views.createNewUser,name='createNewUser'),
    path('AddTask/',views.AddTask,name='AddTask'),
    path('EditTask/<int:id>/',views.EditTask,name='EditTask'),
    path('DeleteTask/<int:id>/', views.DeleteTask, name='DeleteTask'),
    path('MarkComplete/<int:id>/', views.MarkComplete, name='MarkComplete'),
]
