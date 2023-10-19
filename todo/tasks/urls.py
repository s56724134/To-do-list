from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('list', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'), 
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('register', views.registeruser, name='registeruser'),  
]
